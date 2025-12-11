__init__.py: Makes src a Python package.
config.py: Centralized configuration.
Defines constants like YEARS, DATA_DIR, STORAGE_DIR.
Loads environment variables (e.g., GOOGLE_API_KEY) from .env or system env.
Handles API key validation with graceful fallbacks.
data_loader.py: Handles data ingestion.
Loads UBER HTML files using UnstructuredReader.
Adds metadata (e.g., year) and returns document sets.
index_manager.py: Manages vector indices.
Creates/persists indices using LlamaIndex with Google embeddings and LLM.
Loads indices from disk for reuse.
ageny.py: AI agent and tools setup (note: named ageny.py as per your request).
Creates query engine tools for each year's data.
Sets up the SubQuestionQueryEngine and FunctionAgent with the system prompt.
Includes the async chat loop (run_chat).
cli.py: Command-line interface.
Uses argparse for commands: --load-data (index data) and --chat (start interactive chat).
Imports modules relatively and orchestrates the workflow.
custom_console.py: Console utilities.
Functions for clearing screen, spinners, timers, and colored output.
google_llm_init.py: Google LLM initialization.
Sets up the GoogleGenAI LLM instance with the API key.