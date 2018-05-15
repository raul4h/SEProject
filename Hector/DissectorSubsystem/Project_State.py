import gc
from StartBlock import *
from ProtocolDecisionTree import *

class Project_State:

	def __init__(self, type, new, passedBlock):
		tree = self.BuildTree(type, new, passedBlock)

	def BuildTree(self, typeOfBlock, new, passedBlock):
		blockType = typeOfBlock
		info = self.enteringInfo(blockType, new, passedBlock)
		
	def enteringInfo(self, blockType, new, passedBlock):
		type    = blockType
		isNew   = new
		toBuild = passedBlock
		
		
		if isNew == True:
			print "creating: " + type
			creatB = self.createBlock(type, toBuild)
			
		elif isNew == False:
			print "building: " + type
			creatB = self.modifyBlock(type, toBuild)
			
		else:
			print "Unknown Block Type: please read source file Project_State: ENTERING INFO."
			
			
			
	def createBlock(self, type, passedBlock):
		if type.lower() == "field":
			print "1"
			
		elif type.lower() == "decision":
			print "2"
			
		elif type.lower() == "expression":
			print "3"
			
		elif type.lower() == "start":
			print "4"
			
		elif type.lower() == "connector":
			print "5"
			
		elif type.lower() == "endBlock":
			print "6"
			
		else:
			print "Error: Miscommunication in Project State: createBlock and enteringInfo."
			
			
			
			
	def modifyBlock(self, type, passedBlock):
		if type.lower() == "field":
			print "A"
			
		elif type.lower() == "decision":
			print "B"
			
		elif type.lower() == "expression":
			print "C"
			
		elif type.lower() == "start":
			print "D"
			
		elif type.lower() == "connector":
			print "E"
			
		elif type.lower() == "endBlock":
			print "F"
			
		else:
			print "Error: Miscommunication in Project State: modifyBlock and enteringInfo."
		
			