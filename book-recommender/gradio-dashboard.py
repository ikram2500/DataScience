import pandas as pd 
import numpy as np
from dotenv import load_dotenv
from typing import Optional  # add this import

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

import gradio as gr
import os 

api_key =os.getenv("OPENAI_API_KEY", "")
#load_dotenv()

books = pd.read_csv("books_with_emotions.csv")
books["large_thumbnail"] = books["thumbnail"] + "&fife=w800"
books["large_thumbnail"] = np.where(
    books["large_thumbnail"].isna(), 
    "cover not found", 
    books["large_thumbnail"]
    )

raw_documents = TextLoader("tagged_description.txt", encoding='utf-8').load()
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=0, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db_books = Chroma.from_documents(
    documents, OpenAIEmbeddings()
)

def retrieve_semantic_recommendations(
        query: str,
        category: Optional[str] = None,  # changed here
        tone: Optional[str] = None,      # changed here
        initial_top_k: int = 50,
        final_top_k: int = 16
        ) -> pd.DataFrame:
    # Your implementation here
    recs = db_books.similarity_search(query, k=initial_top_k)
    books_list =  [int(rec.page_content.strip('"').split()[0]) for rec in recs]
    book_recs = books[books["isbn13"].isin(books_list)].head(initial_top_k)


    if category != "All":
        book_recs = book_recs[book_recs["simple_categories"] == category].head(final_top_k)

    else:
        book_recs = book_recs.head(final_top_k)

    if tone == "Happy":
        book_recs.sort_values(by="joy", ascending=False, inplace=True)
    elif tone == "Sad":
        book_recs.sort_values(by="sadness", ascending=False, inplace=True)
    elif tone == "Angry":
        book_recs.sort_values(by="anger", ascending=False, inplace=True)
    elif tone == "Fearful":
        book_recs.sort_values(by="fear", ascending=False, inplace=True)

    return book_recs

def recommend_books(
        query: str,
        category: str,
        tone: str 
        ):
    recommendations =  retrieve_semantic_recommendations(
        query, category, tone
    )

    results = []
    for _, row in recommendations.iterrows():
        description = row["description"]
        truncated_desc_split = description.split()
        truncated_description = " ".join(truncated_desc_split[:30]) + "..."

        authors_split = row["authors"].split(";")
        if len(authors_split) == 2:
            authors_str = f"{authors_split[0]} and {authors_split[1]} "
        elif len(authors_split) > 2:
            authors_str = f"{', '.join(authors_split[:-1])}, and {authors_split[-1]}"
        else:
            authors_str = row["authors"]

        caption = f"row[{row['title']} by {authors_str}]: {truncated_description}"
        results.append((row["large_thumbnail"], caption))

    return results 
categories = ["All"] + sorted(books["simple_categories"].unique())
tones = ["All"] + ["Happy", "Sad", "Angry", "Fearful"]

with gr.Blocks() as dashboard:
    gr.Markdown("# Semantic Book Recommender with Emotions")

    with gr.Row():
        user_query = gr.Textbox(label= "Please enter a description of the book",
                                placeholder="A story forgiveness")
        category_dropdown = gr.Dropdown( choices=categories, label = "select category", value="All")
        tone_dropdown = gr.Dropdown(choices=tones, label="select tone", value="All")
        submit_button = gr.Button("Find Recommendations")

    gr.Markdown("## Recommendations")
    output = gr.Gallery(
        label="Recommended Books", columns= 8 , rows= 2,)
    
    submit_button.click( fn=recommend_books,
                        inputs=[user_query, category_dropdown, tone_dropdown],
                        outputs=output)

if __name__ == "__main__":
    dashboard.launch()