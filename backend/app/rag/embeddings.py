from langchain_ollama import OllamaEmbeddings
from app.config import settings

class EmbeddingService:
    def __init__(self):
        self.model = OllamaEmbeddings(model=settings.embedding_model,base_url=settings.ollama_base_url,)
    
    def get(self):
        return self.model