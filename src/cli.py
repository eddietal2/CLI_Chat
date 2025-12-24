"""
Main program for CLI Chat.

Available commands:
  --load-data    Load and index UBER data
  --chat         Start interactive chat
  --verbose, -v  Enable verbose output

Usage examples:
  python -m src.cli --load-data          # Load and index data
  python -m src.cli --chat               # Start chat interface
  python -m src.cli --chat --verbose     # Start chat with verbose output
  python -m src.cli --load-data --verbose # Load data with verbose output
"""

import argparse
import asyncio
from . import custom_console
from .data_loader import load_documents
from .index_manager import setup_indices, load_indices
from .ageny import create_agent, run_chat

def main():
    custom_console.clear_console()
    custom_console.start_process_timer()

    parser = argparse.ArgumentParser(description="Gemi Chat CLI for UBER SEC Analysis")
    parser.add_argument("--load-data", action="store_true", help="Load and index UBER data")
    parser.add_argument("--chat", action="store_true", help="Start interactive chat")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.load_data:
        print("Loading data...")
        doc_set, _ = load_documents()
        setup_indices(doc_set)
        print("Data loaded and indexed.")
    elif args.chat:
        print("Loading indices...")
        index_set = load_indices()
        # Note: Need to create tools here or in agent.py. For now, assuming agent.py handles it.
        # This is incomplete; full refactor needed.
        agent = create_agent(index_set, verbose=args.verbose)
        asyncio.run(run_chat(agent))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
