from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def ask(self, prompt: str) -> str:
        """Return full response (legacy)"""
        pass

    @abstractmethod
    def stream(self, prompt: str):
        """Yield response tokens/chunks as they arrive"""
        yield
