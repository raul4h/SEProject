class ProtocolDecisionTree:
	
	def __init__(self):
		self.blocks = {}
		#registerBlock(self)
		self.counter=1
		
	def setBlock(self,block):
		self.blocks[self.counter] = block
		self.counter = self.counter+1