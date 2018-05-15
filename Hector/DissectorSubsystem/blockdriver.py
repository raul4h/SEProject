import gc
from Block import *

bob = Block("bob", "true")
print bob.Name()

gc.collect()