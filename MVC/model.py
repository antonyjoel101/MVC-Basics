class createfile:
    def __init__ (self,filename,content):
        self.filename=filename+".txt"
        self.content=content
    def create(self):
        with open(self.filename,"w") as file:
            return
    def write(self):
        with open(self.filename,"a") as file:
            file.write(self.content)
            return 
    def read(self):
        with open(self.filename,"r") as file:
            result=file.read()
            return result