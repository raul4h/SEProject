from Block import *

class FieldBlock(Block):

		
    def __init__(self, name, req, inf, ab, fdesc, dataT, base2, masck,cons,  siz):
        Block.__init__(self,name, req)
        self.setInfo(inf)
        self.setAbbr(ab)
        self.setDesc(fdesc)
        self.setType(dataT)
        self.setBase(base2)
        self.setMask(masck)
        self.setConstraint(cons)
        self.setSize(siz)
		
	
		

    def setInfo(self, information):
        self.info = information
		
    def setAbbr(self, abbrev):
        self.abbr = abbrev
		
    def setDesc(self, descrip):
        self.desc = descrip
		
    def setType(self, type1):
        self.types = type1
			
    def setBase(self, base1):
        self.base = base1
		
    def setMask(self, masks):
        self.mask=masks
    
    def setConstraint(self, constraints):
        self.Constraint = constraints
		
    def setSize(self, sizes):
        self.size= sizes	

    def setIsEnd(self, end):
        self.isEnd=end	
	
	
    def getInfo(self):
        return self.info
		
    def getAbbr(self):
        return self.abbr
		
    def getDesc(self):
        return self.desc
		
    def getType(self):
        return self.types
		
    def getBase(self):
        return self.base
		
    def getMask(self):
        return self.mask
    
    def getConstraint(self):
        return self.Constraint
		
    def getSize(self):
        return self.size	

    def getIsEnd(self):
        return self.isEnd

    def getType(self):
        return "FieldBlock"
    	