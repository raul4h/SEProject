import gc
from StartBlock import *

bob = StartBlock("bob", "true", "i hate this")
print bob.Name()
print bob.getDescript()

gc.collect()