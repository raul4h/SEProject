import dicttoxml
import xmltodict
import untangle 
import gc
from StartBlock import *
from FieldBlock import *
from EndBlock import *
from Connector import *
from DecisionBlock import *
from ProtocolDecisionTree import *

class temporaryFormat:
	"""docstring for ClassName"""
	def __init__(self, xml):
		self.xml = xml
	
	
	
	


	def ObjectToXML(object):
		dictionary = object.__dict__
		xml = dicttoxml.dicttoxml(dictionary)
		self.xml = xml
		return xml
	
	def dictionarytoXML(dictionary):
		xml = dicttoxml.dicttoxml(dictionary)
		self.xml = xml
		return xml			
		

	def rebuildDictionary(self, dictionary):
		newDictionary = {}
		print dictionary
		print "hello"
		print type(dictionary)
		for x in dictionary:
			if(dictionary[x]["@type"] == "str"):
				newDictionary[x] = dictionary[x]["#text"]
			elif(dictionary[x]["@type"] == "int"):
				newDictionary[x] = int(dictionary[x]["#text"])
			elif(dictionary[x]["@type"] == "float"):
				newDictionary[x] = float(dictionary[x]["#text"])
			elif(dictionary[x]["@type"] == "bool"):
				newDictionary[x] = bool(dictionary[x]["#text"])
			elif(dictionary[x]["@type"] == "list"):
				newList = []
				print "hey"
			elif(dictionary[x]["@type"] == "dict"):
				    tempDictionary = {}
				    print type(dictionary[x])
				    for k, v in dictionary[x].items():
                        
				    	self.rebuildDictionary(v)




def buildDictionary(self, xml):
		a = xmltodict.parse(xml)
		d = xmltodict.parse(xml, xml_attribs=True)

P=ProtocolDecisionTree()

bob = StartBlock("Start Point", "true", "this spot starts")
P.setBlock(bob)

#print P.blocks.values()[0].Name()
mindy = FieldBlock("mindy", "false", "i hate this even more","min", "this is lame", "app dec block" , "8", None,"none", 8 )
P.setBlock(mindy)

mindyB = FieldBlock("mindyB", "false", "i hate this even more","min", "this is lame", "app dec block" , "8", None,"none", 8 )
P.setBlock(mindyB)

connector1 =  Connector("connector1", "False",P.blocks[1], P.blocks[2] )
P.setBlock(connector1)
connector2 =  Connector("connector2", "False",P.blocks[1], P.blocks[3] )
P.setBlock(connector2)

comp1 = DecisionBlock("IsEqual", False,17, "==",17)
P.setBlock(comp1)

beef = EndBlock("beef", "false")
P.setBlock(beef)

noBeef = EndBlock("no beef", "false")
P.setBlock(noBeef)

connector3 =  Connector("connector3", "False",P.blocks[6], P.blocks[7] )
P.setBlock(connector3)
connector4 =  Connector("connector4", "False",P.blocks[6], P.blocks[8] )
P.setBlock(connector4)

P.blocks[6].setLeftOut(P.blocks[9])

dictionary = bob.__dict__
dictionary1 = mindy.__dict__
dictionary2 = beef.__dict__
xml = dicttoxml.dicttoxml(dictionary)
xml1 = dicttoxml.dicttoxml(dictionary1)
xml2 = dicttoxml.dicttoxml(dictionary2)
print "Convert tree to xml"
print xml
print xml1
print xml2
dictionaryone = xmltodict.parse(xml)
dictionarytwo = xmltodict.parse(xml1)
dictionarythree = xmltodict.parse(xml2)
#print dictionary1 
print "\n"
print "Convert xml to tree"
print dictionaryone
print dictionarytwo
print dictionarythree

tF = temporaryFormat(xml)


