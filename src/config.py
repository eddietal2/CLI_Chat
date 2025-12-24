import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
try:
    load_dotenv(encoding='utf-8')
except Exception as e:
    print(f"Warning: Failed to load .env file with utf-8: {e}. Trying with latin-1...")
    try:
        load_dotenv(encoding='latin-1')
    except Exception as e2:
        print(f"Warning: .env file has encoding issues. Skipping dotenv loading: {e2}")

# Configuration settings
YEARS = [2019, 2020, 2021, 2022]
DATA_DIR = Path("./data/UBER")
STORAGE_DIR = Path("./storage")
SYSTEM_PROMPT_FILE = Path("system_prompt.txt")

# Environment variables
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY not set. Please set it in a .env file or environment variable.")
    print("You can get an API key from: https://makersuite.google.com/app/apikey")
    GOOGLE_API_KEY = None  # Or handle gracefully

# LlamaIndex settings
CHUNK_SIZE = 512
