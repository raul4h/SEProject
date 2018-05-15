import dicttoxml
import xmltodict
import untangle 


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

dictionary = {"name" : "Ana", "age": 22, "gender" : "Female", "Favorite Restraunts" : {"PF changs" : "Chinese", "Carinos": "Italian", "Raising Canes" : "Fast Food", "Kaedama" : "Japanese"}}
xml = dicttoxml.dicttoxml(dictionary)
print "Convert tree to xml"
print xml
dictionary1 = untangle.parse(xml)
dictionary2 = xmltodict.parse(xml)
#print dictionary1 
print "\n"
print "Convert xml to tree"
print dictionary2
tF = temporaryFormat(xml)


