# Prompt2sql
prompt2sql is an intelligent query generation tool that converts natural language prompts into executable SQL queries using Large Language Models (LLMs). This repository is designed to bridge the gap between non-technical users and databases by enabling intuitive, conversational access to structured data.

🚀 Features
🔍 Convert plain English prompts into accurate SQL queries
🧠 Powered by LLMs for semantic understanding and context-aware query generation
🗄️ Supports database schemas and dialects (e.g., MySQL)
🛠️ Easy integration with existing data pipelines or analytics dashboards
🧪 Includes test cases and examples for common query patterns
📦 Use Cases
Business intelligence tools
Data exploration for non-technical users
Chatbot interfaces for databases

1. Install Ollama
For Windows / macOS / Linux:
Go to the official website and download the installer:

👉 https://ollama.com/download

Windows: Runs as a background service (ollama.exe)

macOS: Comes as .dmg

Linux (Debian/Ubuntu):

curl -fsSL https://ollama.com/install.sh | sh

After installation, run:
ollama --version
To confirm it’s working.

✅ 2. Run a Model
Ollama comes with a simple CLI to pull and run models:

Example (to pull and run LLaMA3):

ollama run mistral:latest

You can check all available models at: https://ollama.com/library

✅ 3. Optional Python API (if you want to use it in code)
Install the Python client:

pip install ollama

✅ 4. System Requirements
At least 8–16 GB RAM
Modern CPU (GPU not required, but speeds up processing if supported)
Disk space: each model can be several GBs

🔁 Commands You Might Need
List models:
ollama list
ollama rm llama3

Pull model manually (without running):
ollama pull llama3
