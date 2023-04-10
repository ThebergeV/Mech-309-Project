"""

@author: Vincent
"""
import numpy as np
import math
from Question_4 import *
from Question_7 import *

h = 1
domain = findDomain(-200, 200, h)




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

#for a parameter b, runs the code of question 3 and 4 to find the length of the curve
numb =0
minCurve = 9999999999999999999999999
maxCurve = 0
l0 = 0
for i in completeDomain:
    a = Newton([1, 1, 1], i)
    if numb != 0:
        l =0
        l = findLength(a, h, i)
        l0 = l
        #Replaces the value of a if it give the minimum length of the curve or the maximum
        if (l < minCurve):
            minCurve = l
            bMin = i
        if (l > maxCurve):
            maxCurve = l
            bMax = i
    numb +=1
    try:
        print("b: " + str(i))
        print("lenght: " + str(l))
        print("The value of b to get minimum is: " + str(bMin))
        print("The value of b to get maximum is: " +str(bMax))
    except:
        print("No critical values for now")

j = 0
preciseDomain = np.empty(1)
while j < 1000:

    preciseDomain = np.append(preciseDomain, [bMin + 0.001*j])
    preciseDomain = np.append(preciseDomain, [bMin - 0.001*j])
    preciseDomain = np.append(preciseDomain, [bMax + 0.001*j])
    preciseDomain = np.append(preciseDomain, [bMax - 0.001*j])

numb = 0
for i in preciseDomain:
    a = Newton([1, 1, 1], b)
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
        print("b: " + str(i))
        print("lenght: " + str(l))
        print("The value of b to get minimum is: " + str(bMin))
        print("The value of b to get maximum is: " +str(bMax))
    except:
        print("No critical values for now")