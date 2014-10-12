import os
class WriteFile:
    reference = None
    file_path = None
    basename = None
    basepath = None
    file_size = 0
    
    
    def __init__(self, file_path):
        
    
        try:
            self.file_path = file_path
            self.reference = open(file_path, 'w+')
            self.basename = os.path.basename(file_path)
            self.file_size = os.path.getsize(file_path)
            
            #remove file name from path
            basepath = self.file_path.replace(self.basename, '')
            last_char = basepath[-1]
            
            #if there is a trailing slash remove it
            if last_char == '/':
                self.basepath = basepath[:-1]
        
        except Exception as e:
            raise Exception("Write File exception %s on %s"  % (e, file_path))        
            
            
    #read file sizes change. use os.path.getsize
    def getSize(self):
        if os.path.exists(self.file_path):
            size = os.path.getsize(self.file_path)
            self.file_size = size
            return self.file_size
        else:
            raise Exception("Write File %s does not exist"  % self.file_path)
    
    def getBasename(self):
        return self.basename
    
    def getFullPath(self):
        return self.file_path
    
    def getBasepath(self):
        return self.basepath
    
    def getReference(self):
        return self.reference
            
            