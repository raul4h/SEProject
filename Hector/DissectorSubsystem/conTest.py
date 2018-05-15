import gc
from StartBlock import *
from FieldBlock import *
from EndBlock import *
from Connector import *
from ProtocolDecisionTree import *

P=ProtocolDecisionTree()

bob = StartBlock("bob", "true", "i hate this")

P.setBlock(bob)

#print P.blocks.values()[0].Name()

mindy = FieldBlock("mindy", "false", "i hate this even more","min", "this is lame", "app dec block" , "8", None,"none", 8 )
P.setBlock(mindy)

beef = EndBlock("beef", "false")
P.setBlock(beef)

connector1 =  Connector("connector1", "False",P.blocks[1], P.blocks[2] )
P.setBlock(connector1)
connector2 =  Connector("connector2", "False",P.blocks[2], P.blocks[3] )
P.setBlock(connector2)

for i in range(len(P.blocks)):
		print str(i+1) +", "+ P.blocks[i+1].getType()+":"+P.blocks[i+1].Name()
	
#print bob.getDescript()
#print P.blocks[2].Name()
#print P.blocks[2].getDescript()

gc.collect()