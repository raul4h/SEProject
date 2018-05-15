from Block import *

class Connector(Block):
	def __init__(self, name, req, past, future):
		Block.__init__(self,name, req)
		self.before = past
		self.to = future
		self.value =None
		print "values were" + past.Name() + future.Name()

	def geTo(self):
		return self.to
	def getFrom(Self):
		return self.before
	def getType(self):
		return "Connector"
	def getType(self):
		return self.before.Name() +" is Connected to " +self.to.Name()+"."
	def setValue(self, val):
		self.value=val
	def getValue(self):
		return self.value
		