# CLI AI Coding Agent

## Introduction

CLI AI Coding Agent using AI to read, edit, and improve Python code with support for multiple AI backends including Gemini, OpenAI, Claude, and Ollama. It allows you to safely edit Python files with backups, see streaming output for live code edits, and use system prompts for consistent behavior.

## Features

Supports multiple AI models Gemini, OpenAI, Ollama, and Claude. Edit Python files safely with backup. Streaming output for live code edits with OpenAI. CLI flags for automatic application --yes and file input --file. System prompt templates for consistent AI behavior.

## Installation

Clone the repository and navigate into it

```bash
git clone https://github.com/yourusername/AI_Agent.git
cd AI_Agent 
```

## Create a virtual environment and install the required

```bash 
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt

```

## Copy .env.example to .env and add your API keys

```bash
cp .env.example .env
```

# Usage

## Edit a python file

```bash
python main.py "Refactor this function" --file my_script.py --model openai --yes
```

## Run normal CLI mode without a file

```bash
python main.py "Explain Python decorators" --model claude
```

Streaming output is enabled by default for OpenAI/ Use --no-stream to disable


