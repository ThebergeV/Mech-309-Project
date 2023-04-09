"""
Created on Sat Mar 18 14:10:57 2023

@author: Anika
"""

import numpy as np
import math
from Question_4 import *
from Question_7 import *

domain = findDomain(-200, 200)
#Example for gitHub
minCurve = 9
maxCurve = -1
a = [1, 1, 1]
error = 9999
h = 1


def criticalPoints(a, h):
    touch = False
    zerosInARow = 0
    criticalPointMin1 = 99999999999999999999
    dCriticalMin1 = 0
    criticalPointMax = 0
    dCriticalMax = 0
    for i in range(d, 999999, 0.001):
        l = findLength(a, h, i)
        if l > 0 and (l < criticalPointMin1 or l < criticalPointMin2):
            touch = True
            if criticalPointMin1 < criticalPointMin2:
                dCriticalMin1 = i
            else:
                dCriticalMin2 = 1
        elif l > 0 and l > criticalPointMax:
            touch = True
            dCriticalMax = i

        elif l == 0 and touch == True:
            zerosInARow += 1
            if zerosInARow >= 10:
                return [dCriticalMin1, dCriticalMax, dCriticalMin2]
    return [dCriticalMin1, dCriticalMax]



#for a parameter a, runs the code of question 3 and 4 to find the length of the curve
for i in range(min(domain), max(domain)):
    l = findLength(, h)
    errorMin = 0
    errorMax = 0
    #Replaces the value of a if it give the minimum length of the curve or the maximum
    if (minCurve < 0 or l < minCurve):
        errorMin = abs(minCurve - l)
        minCurve = l
        aMin = h
    if (maxCurve < 0 or l > maxCurve):
        errorMax = abs(maxCurve - l)
        maxCurve = l
        aMax = h
    error = max(errorMin, errorMax)
    h = h + error
