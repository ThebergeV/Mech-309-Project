"""

@author: Vincent
"""
import numpy as np
import math
from Question_4 import *
from Question_7 import *

h = 1
domain = findDomain(-200, 200, h)

h0= 0.01
def preciseDomain(step, bMin, bMax):
    j = 0
    preciseDomain = np.empty(0)
    while j < 10:
        preciseDomain = np.append(preciseDomain, [bMin + (step*j)])
        preciseDomain = np.append(preciseDomain, [bMin - (step*j)])
        preciseDomain = np.append(preciseDomain, [bMax + (step*j)])
        preciseDomain = np.append(preciseDomain, [bMax - (step*j)])
        j+=1
    print(preciseDomain)
    return preciseDomain

def critVal(inputDomain):
    minCurve = 9999999999999999999999999
    maxCurve = 0
    l0 = 0
    for i in inputDomain:
        a = Newton([1, 1, 1], i)
        if str(i) != "nan":
            l =0
            l = findLength(a, h0, i)
            l0 = l
            #Replaces the value of a if it give the minimum length of the curve or the maximum
            if (l < minCurve and l != 0):
                minCurve = l
                bMin = i
            if (l > maxCurve):
                maxCurve = l
                bMax = i
        try:
            print("b: " + str(i))
            print("lenght: " + str(l))
            print("The value of b to get minimum is: " + str(bMin))
            print("The value of b to get maximum is: " +str(bMax))
        except:
            print("No critical values for now")
    return [bMin, bMax]



domainSize = domain.__len__()

j = 0
completeDomain = np.empty(1)
while j < domainSize:
    start = domain[j][0]
    stop = domain[j].__len__()-1 + start
    value = 0
    while start <= stop:
        value = start
        completeDomain = np.append(completeDomain, [value])
        start += 1
    j += 1

print(completeDomain)

criticalValues1 = critVal(completeDomain)

domain2 = preciseDomain(0.1, criticalValues1[0], criticalValues1[1])
criticalValues2 = critVal(domain2)

domain2 = preciseDomain(0.01, criticalValues2[0], criticalValues2[1])
criticalValues2 = critVal(domain2)

domain3 = preciseDomain(0.001, criticalValues2[0], criticalValues2[1])
criticalValues3 = critVal(domain3)