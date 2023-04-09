"""
Created on Sat Mar 18 14:10:57 2023

@author: Anika
"""

import numpy as np
import math
from Question_4 import *
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



for i in range(d, 999999999999999999999999, 1) :
    l = findLength(a, h)
    if l > 0:
        criticalPoints(a, h)
        skip
