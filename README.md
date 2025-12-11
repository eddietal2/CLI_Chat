# Notta Advisor

💬 Concept
Notta Advisor is a portfolio project designed to showcase advanced AI engineering techniques, primarily Retrieval-Augmented Generation (RAG) and Agentic Design, within a full-stack web application.

The application functions as a personalized investment analysis tool that critically assesses current market data against foundational financial wisdom. Analysis is run manually on demand.

# Key Features

Agentic Workflow: The core of the project is an AI Agent built with Llama Index and powered by the Gemini API. This agent can autonomously plan, reason, and execute multi-step tasks.

# Multi-Modal Data Ingestion (RAG & Tools):

RAG (Fundamental Wisdom): The Agent is grounded in the principles of value investing by indexing and retrieving information from the classic text, "The Intelligent Investor."

Tool Use (Market Data): The Agent uses a custom Python function (built with yfinance) to fetch real-time and historical data for key high-growth stocks ("Mag 10").

Full-Stack Delivery (Django): The application is built on Django, providing a robust framework for:

User Management: Collecting and persisting user subscriptions via a simple one-page interface.

Manual Analysis: Run the analysis on demand using Django management commands.

Personalization: Tailoring the analysis based on user-selected investment interests (e.g., emphasizing Growth Stocks vs. Risk).

Email Delivery: The final, synthesized analysis is delivered directly to subscribers via email.

# Goal
To demonstrate expertise in building a data-driven AI system that moves beyond simple Q&A and into complex, reasoned task execution.

Disclaimer: Notta Advisor is for educational and illustrative purposes only and does not constitute financial advice.