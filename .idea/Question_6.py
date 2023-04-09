"""

@author: Vincent
"""
import numpy as np
import math
from Question_4 import *
from Question_7 import *

h = 1
domain = findDomain(-200, 200, h)

a = [1, 1, 1]


domainSize = domain.__len__()
print("domain size: "+ str(domainSize))

j = 0
completeDomain = np.empty(1)
while j < domainSize:
    start = domain[j][0]
    stop = domain[j][1]
    value = 0
    while start <= stop:
        value = start
        completeDomain = np.append(completeDomain, [value])
        start += 0.001
    j += 1

print(completeDomain)
#for a parameter b, runs the code of question 3 and 4 to find the length of the curve
numb =0
minCurve = 9999999999999999999999999
maxCurve = 9999999999999999999999999
for i in completeDomain:
    if numb != 0:
        l = findLength(a, h, i)
        #Replaces the value of a if it give the minimum length of the curve or the maximum
        if (l < minCurve):
            minCurve = l
            bMin = i
        if (l > maxCurve):
            maxCurve = l
            bMax = i
    numb +=1
    try:
        print(str(i))
        print("The value of b to get minimum is: " + str(bMin))
        print("The value of b to get maximum is: " +str(bMax))
    except:
        print("No critical values for now")