from Block import *

class EndBlock(Block):

    def __init__(self, name, req):
        Block.__init__(self,name, req)
		
		
    def getType(self):
        return "EndBlock"