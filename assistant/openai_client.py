import os
import openai
from dotenv import load_dotenv
from assistant.base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self):
        load_dotenv()
        openai.api_key = os.environ["OPENAI_API_KEY"]

    def ask(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # free-tier compatible
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
    
    def stream(self, prompt: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        for event in response:
            if event['choices'][0]['delta'].get('content'):
                yield event['choices'][0]['delta']['content']

