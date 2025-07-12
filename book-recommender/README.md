# 📚 Semantic Book Recommender with Emotions

A sophisticated book recommendation system that combines semantic search with emotion analysis to provide personalized book suggestions based on user preferences and desired emotional tone.

## 🚀 Features

- **Semantic Search**: Uses OpenAI embeddings and Chroma vector database for intelligent book matching
- **Emotion-Based Filtering**: Recommends books based on emotional tone (Happy, Sad, Angry, Fearful)
- **Category Filtering**: Filter recommendations by book categories
- **Interactive Web Interface**: Built with Gradio for easy user interaction
- **Rich Book Metadata**: Displays book covers, descriptions, and author information

## 🛠️ Technologies Used

- **Python 3.11+**
- **LangChain**: For document processing and embeddings
- **OpenAI Embeddings**: For semantic search capabilities
- **Chroma**: Vector database for similarity search
- **Gradio**: Web interface framework
- **Pandas & NumPy**: Data manipulation and analysis
- **Transformers**: For emotion analysis

## 📋 Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Required Python packages (see requirements.txt)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd book-recommender
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 📊 Data Files

The project requires the following data files:
- `books_with_emotions.csv`: Main dataset with book metadata and emotion scores
- `tagged_description.txt`: Text file with book descriptions for vector indexing

## 🚀 Usage

1. **Start the Gradio interface**
   ```bash
   python gradio-dashboard.py
   ```

2. **Access the web interface**
   - Open your browser and go to the URL shown in the terminal (typically `http://127.0.0.1:7860`)

3. **Get recommendations**
   - Enter a description of the type of book you're looking for
   - Select a category (optional)
   - Choose an emotional tone (optional)
   - Click "Find Recommendations"

## 🔍 How It Works

1. **Vector Search**: User queries are converted to embeddings and compared against a vector database of book descriptions
2. **Filtering**: Results are filtered by category and sorted by emotional tone if specified
3. **Ranking**: Books are ranked by similarity score and emotion intensity
4. **Display**: Top recommendations are displayed with covers and descriptions

## 📁 Project Structure

```
book-recommender/
├── gradio-dashboard.py      # Main application file
├── requirements.txt         # Python dependencies
├── books_with_emotions.csv  # Book dataset with emotion scores
├── tagged_description.txt   # Book descriptions for indexing
├── data_extraction.ipynb    # Data preprocessing notebook
├── sentiment-analysis.ipynb # Emotion analysis notebook
├── text_classification.ipynb # Text classification experiments
├── vector_search.ipynb     # Vector search experiments
└── README.md               # This file
```

## 🎯 Key Functions

- `retrieve_semantic_recommendations()`: Core function for semantic search and filtering
- `recommend_books()`: Formats recommendations for the UI
- Vector database initialization with Chroma and OpenAI embeddings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🚨 Important Notes

- Ensure you have a valid OpenAI API key for embeddings
- The application requires the emotion-analyzed book dataset
- Vector database will be created on first run (may take some time)

## 🐛 Troubleshooting

### Common Issues

1. **Missing API Key**: Make sure your OpenAI API key is set in the `.env` file
2. **Module Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Data File Errors**: Verify that `books_with_emotions.csv` and `tagged_description.txt` exist in the project directory

### Performance Tips

- The initial vector database creation may take several minutes
- For better performance, consider using a GPU-enabled environment
- Adjust `initial_top_k` and `final_top_k` parameters based on your needs

## 📧 Support

If you encounter any issues or have questions, please open an issue in the repository.

---

**Happy Reading! 📖✨**
