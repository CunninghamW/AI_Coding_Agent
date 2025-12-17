import os
from dotenv import load_dotenv
from google import genai
from assistant.base import LLMClient

class GeminiClient(LLMClient):
    def __init__(self):
        load_dotenv()
        self.client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"]
        )

    def ask(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text

