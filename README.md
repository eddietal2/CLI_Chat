# Gemi Chat 🤖

A CLI-based AI chatbot for analyzing UBER SEC 10-K filings using Retrieval-Augmented Generation (RAG) and Google's Gemini API.

## 🚀 Features

- **AI-Powered Analysis**: Interactive chat with a FunctionAgent that answers questions about UBER's financial data from 2019-2022.
- **RAG with LlamaIndex**: Indexes SEC filings for accurate, context-aware responses.
- **CLI Interface**: Simple command-line tools for data loading and chatting.
- **Modular Design**: Clean, maintainable code structure for easy extension.

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/gemi-chat.git
   cd gemi-chat
   ```

2. **Install dependencies** (using uv for speed):
   ```bash
   uv sync
   ```

3. **Set up environment**:
   - Create a `.env` file: `GOOGLE_API_KEY=your_gemini_api_key`
   - Or set the env var: `$env:GOOGLE_API_KEY = "your_key"`

## 🛠️ Usage

- **Load and index data**:
  ```bash
  python -m src.cli --load-data
  ```

- **Start interactive chat**:
  ```bash
  python -m src.cli --chat
  ```

- **View help**:
  ```bash
  python -m src.cli --help
  ```

Example chat: Ask questions like "What were UBER's revenue trends in 2020?" and get AI-powered answers based on the filings.

## 📁 Project Structure

```
Gemi_Chat/
├── src/                          # Main package
│   ├── __init__.py              # Package init
│   ├── config.py                # Settings & env vars
│   ├── data_loader.py           # Loads UBER HTML data
│   ├── index_manager.py         # Manages vector indices
│   ├── ageny.py                 # AI agent & tools
│   ├── cli.py                   # Command-line interface
│   ├── custom_console.py        # Console utilities
│   └── google_llm_init.py       # Gemini LLM setup
├── pyproject.toml               # Project config & deps
├── system_prompt.txt            # Agent system prompt
├── .env                         # Environment variables
├── data/UBER/                   # UBER SEC filings
└── storage/                     # Persisted indices
```

### Module Details

- **`config.py`**: Centralized configuration (years, paths, API keys).
- **`data_loader.py`**: Data ingestion with UnstructuredReader.
- **`index_manager.py`**: Vector index creation/persistence.
- **`ageny.py`**: Agent setup with query engines and chat loop.
- **`cli.py`**: CLI with argparse for commands.
- **`custom_console.py`**: Spinners, colors, timers.
- **`google_llm_init.py`**: Google Gemini LLM initialization.

## 🤝 Contributing

1. Fork the repo.
2. Create a feature branch.
3. Commit changes.
4. Push and open a PR.

## 📄 License

MIT License - see LICENSE file for details.

## ⚠️ Disclaimer

This is for educational purposes only. Not financial advice.