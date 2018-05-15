from Block import *

class StartBlock(Block):

    def __init__(self, name, req, desc):
        Block.__init__(self,name, req)
        self.description = desc

    def getDescript(self):
        return self.description
		
    def getType(self):
        return "StartBlock"