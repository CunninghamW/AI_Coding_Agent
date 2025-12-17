import os
from assistant.base import LLMClient
import requests
from dotenv import load_dotenv

class ClaudeClient(LLMClient):
    """
    Example wrapper for Claude API v1.
    Make sure you have CLAUDE_API_KEY in your .env
    """
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ["CLAUDE_API_KEY"]
        self.endpoint = "https://api.anthropic.com/v1/complete"

    def ask(self, prompt: str) -> str:
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "model": "claude-v1",
            "prompt": prompt,
            "max_tokens_to_sample": 300
        }
        response = requests.post(self.endpoint, json=data, headers=headers)
        if response.ok:
            return response.json().get("completion", "")
        else:
            return f"Claude API error: {response.status_code} {response.text}"
