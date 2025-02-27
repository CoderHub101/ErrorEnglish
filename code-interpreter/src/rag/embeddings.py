from sentence_transformers import SentenceTransformer

class ErrorEmbeddings:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def get_embeddings(self, text):
        return self.model.encode(text)