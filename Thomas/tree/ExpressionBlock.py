from Block import *

class ExpressionBlock(Block):

	def __init__(self, name, req, left, operator,right ):
		Block.__init__(self,name, req)
		self.leftOp = left
		self.rightOp = right
		self.op= operator


#< > <= >= == != and or !		
#left op is None if its a not comparison 
	
	def getDecision(self):
		if self.op == "==":
			return leftOp == rightOp
		if self.op == "!=":
			return leftOp != rightOp
		if self.op == "<=":
			return leftOp <= rightOp
		if self.op == ">=":
			return leftOp >= rightOp
		if self.op == "and":
			return leftOp and rightOp
		if self.op == "or":
			return leftOp or rightOp
		if self.op == "!":
			return not rightOp
		if self.op == "<":
			return leftOp < rightOp
		if self.op == ">":
			return leftOp > rightOp
		return None



			
		
	def getType(self):
		return "Expression"