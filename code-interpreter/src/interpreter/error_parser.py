from rag.vector_store import ErrorVectorStore

class ErrorParser:
    def __init__(self):
        self.vector_store = ErrorVectorStore()
    
    def parse_error(self, error_dict):
        error_message = f"{error_dict['type']}: {error_dict['message']}"
        friendly_message = self.vector_store.find_similar_error(error_message)
        
        # Extract line number if available
        line_no = self._extract_line_number(error_dict['traceback'])
        if line_no:
            friendly_message = f"At line {line_no}: {friendly_message}"
            
        return friendly_message
    
    def _extract_line_number(self, traceback):
        for line in traceback.split('\n'):
            if 'line' in line:
                try:
                    return line.split('line')[1].split()[0]
                except IndexError:
                    pass
        return None