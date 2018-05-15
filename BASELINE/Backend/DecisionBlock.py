from Block import *
from ExpressionBlock import *

class DecisionBlock(ExpressionBlock):

    def __init__(self, name, req, left, operand, right):
        ExpressionBlock.__init__(self,name, req, left, operand, right)
        self.lLeg = ""
        self.rLeg = ""

    def getResult(self):
        self.lLeg.setValue(self.getDecision())
        self.rLeg.setValue(not(self.getDecision()))

    def setLeftOut(self, l):
        self.lLeg = l
    def setRightOut(self, r):
        self.rLeg = r

    def getLeftValue(self):
        if self.getResult():
            return True
        else:
            return False	
    def getType(self):
        return "DecisionBlock"