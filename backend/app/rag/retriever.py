from typing import Optional
class Retriever:
    def __init__(self, vectorstore, k: int = 5):
        self.vectorstore = vectorstore
        self.k = k

    def retrieve(self, question: str, document_id: Optional[int] = None):
        search_kwargs = {"k": self.k}
        if document_id:
            search_kwargs["filter"] = {"document_id": document_id}
        return self.vectorstore.as_retriever(search_kwargs=search_kwargs).invoke(question)