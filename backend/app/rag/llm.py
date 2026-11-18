from app.config import settings
from langchain_ollama import ChatOllama

llm = ChatOllama(model=settings.llm_model, base_url=settings.ollama_base_url, temperature=0.2)