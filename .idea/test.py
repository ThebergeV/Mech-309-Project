from Question_4 import *
from Question_5 import *

a0 = Newton([1,1,1], 0)
a1 = Newton([1,1,1], -140)

l0 = findLength(a0, 0.1, 0)
l1 = findLength(a1, 0.1, -140)
print(l0)
print(l1)
