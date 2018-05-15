import gc
from StartBlock import *
from ProtocolDecisionTree import *

P=ProtocolDecisionTree()

bob = StartBlock("bob", "true", "i hate this")

P.setBlock(bob)

mindy = StartBlock("mindy", "false", "i hate this even more")
P.setBlock(mindy)



print P.blocks[1].Name()
#print bob.getDescript()
print P.blocks[2].Name()
print P.blocks[2].getDescript()

gc.collect()