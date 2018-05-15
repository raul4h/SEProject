import dicttoxml
import xmltodict
import jsonz


class temporaryFormat:
	"""docstring for ClassName"""
	def __init__(self, xml):
		self.xml = xml
	
	
	
	def buildDictionary(xml):
		a = xmltodict.parse(xml)
		d = xmltodict.parse(xml, xml_attribs=True)


	def ObjectToXML(object):
					
		

	def rebuildDictionary(dictionary):
		newDictionary = {}
		for x in dictionary:
			print dictionary[x]['@type']
			if(dictionary[x]['@type'] == 'str'):
				newDictionary[x] = dictionary[x]['#text']
			elif(dictionary[x]['@type'] == 'int'):
				newDictionary[x] = int(dictionary[x]['#text'])
			elif(dictionary[x]['@type'] == 'float'):
				newDictionary[x] = float(dictionary[x]['#text'])
			elif(dictionary[x]['@type'] == 'bool'):
				newDictionary[x] = bool(dictionary[x]['#text'])
			elif(dictionary[x]['@type'] == 'list'):
				listt = buildList(dictionary[x])
				newDictionary[x] = tempSet
			elif(dictionary[x]['@type'] == 'dict'):
			listt = buildList(dictionary[x])
			newDictionary[x] = listt
		else:
			newDictionary[x] = rebuildDictionary()
			


	return newDictionary



