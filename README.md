# ExcelPilot 📊

ExcelPilot is an intelligent Excel analysis tool that uses Retrieval-Augmented Generation (RAG) with natural language processing to help users analyze and understand their Excel data effortlessly.

## 🌟 Features

- **Natural Language Queries**: Ask questions about your Excel data in plain English
- **Smart Visualization**: Automatic generation of relevant charts and graphs
- **Data Analysis**: Advanced pattern recognition and trend analysis
- **Interactive Interface**: User-friendly Streamlit web interface
- **Sample Data Generation**: Built-in functionality to create sample datasets
- **Multi-table Support**: Handle multiple Excel files simultaneously

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/SamSon1402/ExcelPilot.git
cd ExcelPilot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the application:
```bash
streamlit run app/main.py
```

## 💡 Usage

1. **Upload Data**
   - Use the sidebar to upload your Excel file
   - Or generate sample data using the built-in generator

2. **Ask Questions**
   - Type your questions in natural language
   - Example queries:
     - "What is the average salary by department?"
     - "Show me the performance rating distribution"
     - "Analyze the correlation between experience and salary"

3. **View Results**
   - Get natural language responses
   - Explore automatically generated visualizations
   - Download analysis reports

## 🏗️ Project Structure

```
excel-rag-project/
├── app/
│   ├── __init__.py
│   ├── main.py              # Streamlit application
│   ├── rag_system.py        # RAG implementation
│   ├── data_generator.py    # Sample data generator
│   └── utils/
│       ├── database.py      # Database operations
│       └── visualization.py # Visualization helpers
├── data/
│   └── sample/             # Sample Excel files
├── tests/
└── [Config files]
```

## 🛠️ Development

### Setting Up Development Environment
```bash
pip install -r requirements.txt
```

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black .
flake8
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💫 Technologies Used

- [Streamlit](https://streamlit.io/) - Web interface
- [Google Gemini](https://ai.google.dev/) - Natural language processing
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Plotly](https://plotly.com/) - Data visualization
- [SQLite](https://www.sqlite.org/) - Data storage

## 📞 Support

- Open an issue for bug reports or feature requests
- Check out our [documentation](docs/) for detailed guides
- Email: support@excelpilot.com

## ✨ Acknowledgments

- Google Gemini team for the amazing API
- Streamlit team for the powerful web framework
- All our contributors and users

---
Made with ❤️ by [SamSon1402](https://github.com/SamSon1402)
