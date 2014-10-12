import os
class ReadFile:
    reference = None
    file_path = None
    basename = None
    basepath = None
    file_size = 0
    
    
    def __init__(self, file_path):
        
        if os.path.exists(file_path):
            try:
                self.file_path = file_path
                self.reference = open(file_path, 'r')
                self.basename = os.path.basename(file_path)
                self.file_size = os.path.getsize(file_path)
                
                #remove file name from path
                basepath = self.file_path.replace(self.basename, '')
                last_char = basepath[-1]
                
                #if there is a trailing slash remove it
                if last_char == '/':
                    self.basepath = basepath[:-1]
                    print self.basepath
                    
            except Exception as e:
                raise Exception("Read File exception %s on %s"  % (e, file_path))
                
        else:
           raise Exception("Read File %s does not exist"  % file_path)
            
            
    def getSize(self):
        return self.file_size
    
    def getBasename(self):
        return self.basename
    
    def getFullPath(self):
        return self.file_path
    
    def getBasepath(self):
        return self.basepath
    
    def getReference(self):
        return self.reference
            
            