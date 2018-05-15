import gc
from StartBlock import *
from FieldBlock import *
from EndBlock import *
from Connector import *
from DecisionBlock import *
from ProtocolDecisionTree import *

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
#comp1.setRightOut(P.blocks[10])








#comp1 = ExpressionBlock("IsEqual", False, connector3, connector4,17, "==",17)





for i in range(len(P.blocks)):
		print str(i+1) +", "+ P.blocks[i+1].getType()+":"+P.blocks[i+1].Name()
	
#print bob.getDescript()
#print P.blocks[2].Name()
#print P.blocks[2].getDescript()

gc.collect()