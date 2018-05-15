from Block import *

class Connector(Block):
	def __init__(self, name, req, past, future):
		Block.__init__(self,name, req)
		self.before = past
		self.to = future

	def geTo(self):
		return self.to
		
	def getFrom(Self):
		return self.before