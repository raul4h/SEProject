import gc
from StartBlock import *
from FieldBlock import *
from Connector	import *
from ProtocolDecisionTree import *

class Project_State:


	global Proto
	Proto = ProtocolDecisionTree()
	PDTBlock = []


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
			print "updating: " + type
			creatB = self.modifyBlock(type, toBuild)
			
		else:
			print "Unknown Block Type: please read source file Project_State: ENTERING INFO."
			
			
			
	def createBlock(self, type, passedBlock):
		if type.lower() == "field":
			print "1"
			if(len(passedBlock) == 10):
				adding = FieldBlock(passedBlock[0], passedBlock[1], passedBlock[2], passedBlock[3], passedBlock[4], passedBlock[5], passedBlock[6], passedBlock[7], passedBlock[8], passedBlock[9])
				Proto.setBlock(adding)
				print Proto.blocks[1].getInfo()
				print Proto.blocks[1].getAbbr()
				print Proto.blocks[1].getDesc()
				print Proto.blocks[1].getType()
				print Proto.blocks[1].getBase()
				print Proto.blocks[1].getMask()
			else:
				print "The List size of fields entered for field block are more or less than the size 10"
			
		elif type.lower() == "decision":
			print "2"
			
		elif type.lower() == "expression":
			print "3"
			
		elif type.lower() == "start":
			print "4"
			adding = StartBlock(passedBlock[0], passedBlock[1], passedBlock[2])
			P.setBlock(adding)
			
		elif type.lower() == "connector":
			print "5"
			adding = StartBlock(passedBlock[0], passedBlock[1], passedBlock[2], passedBlock[3])
			P.setBlock(adding)
			
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
		
			