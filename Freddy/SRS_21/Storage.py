import gc


class Storage:
	
		name = " "
		required = None
		past = None
		future = None
		description = " "
		
		def __init__(self):
			name = " "
			required = None
			past = None
			future = None
			description = " "
			
		def getBlockInfo(self):
			list = []
			list = [name, required, past, future, description]
			return list