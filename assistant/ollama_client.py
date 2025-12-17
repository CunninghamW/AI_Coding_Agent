from assistant.base import LLMClient
import subprocess

class OllamaClient(LLMClient):
    def __init__(self, model="mistral"):
        self.model = model

    def ask(self, prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", self.model, prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
