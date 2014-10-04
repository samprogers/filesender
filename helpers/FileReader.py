class FileReader:
    file_reference = None
    
    def __init__(self, file_path):
        self.file_reference = open(file_path, 'r')
        
        
    def read(self, chunk_size=None):
        if chunk_size is None:
            return self.file_reference.read()
        else:
            while True:
                data = file_pointer.read(chunk_size)
                if not data:
                    break
        
                yield data