import chromadb
import json
import os

class ErrorVectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("error_messages")
        self.load_error_messages()
    
    def load_error_messages(self):
        data_path = os.path.join(os.path.dirname(__file__), '../data/error_messages.json')
        with open(data_path, 'r') as f:
            data = json.load(f)
            
        # Add documents to collection
        documents = [msg["original"] for msg in data["error_messages"]]
        metadata = [{"type": msg["type"]} for msg in data["error_messages"]]
        friendly_messages = [msg["friendly"] for msg in data["error_messages"]]
        
        self.collection.add(
            documents=documents,
            metadatas=metadata,
            ids=[str(i) for i in range(len(documents))]
        )
        
        self.friendly_messages = dict(zip(documents, friendly_messages))
    
    def find_similar_error(self, error_message, k=1):
        results = self.collection.query(
            query_texts=[error_message],
            n_results=k
        )
        
        if results and results['documents'][0]:
            most_similar = results['documents'][0][0]
            return self.friendly_messages.get(most_similar, "Unknown error occurred")
        
        return "Unknown error occurred"