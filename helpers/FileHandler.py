import bootstrap, math, time, sys
from ReadFile import ReadFile
from WriteFile import WriteFile
class FileHandler:
    file = None
    chunk_size = 128000
    chunk_data = {}
    number_of_chunks = None
    
    def __init__(self, file_path, chunk_size=None):
        self.file = ReadFile(file_path)
        if chunk_size is not None and isinstance(chunk_size, int):
            self.chunk_size = chunk_size
            
        self.setNumberOfChunks()
        
        
    def getChunkData(self):
        return self.chunk_data
    
    
    def setNumberOfChunks(self):
        file_size = self.file.getSize()
        self.number_of_chunks = math.ceil(float(file_size) / float(self.chunk_size))
        self.number_of_chunks = int(self.number_of_chunks)
        
        
        
    #spit file data and store it in memory
    def split(self, file_path=None):
        
        #if a new file is given load file data
        if file_path is not None:
            self.file = ReadFile(file_path)
            self.setNumberOfChunks()
        
        #loop through number of chunks and store data
        file_reference = self.file.getReference()
        for chunk_index in range(0, self.number_of_chunks):
            self.chunk_data[chunk_index] = file_reference.read(self.chunk_size)
        
    #copy file given the destination path
    def copy(self, out_file_path, in_file_path=None):
        start = time.time()
        if in_file_path is not None:
            self.split(in_file_path)
        else:
            self.split()
        
        output_file = WriteFile(out_file_path)
        output_reference = output_file.getReference()
        
        #loop through chunks and write data
        for chunk_index in range(0, self.number_of_chunks):
            chunk_data = self.chunk_data[chunk_index]
            output_reference.write(chunk_data)
            
        output_reference.close()
        
        

        
                
                
