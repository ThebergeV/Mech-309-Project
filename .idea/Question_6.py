import numpy as np
import math
from Question_4 import *
#Example for gitHub
minCurve = -1
maxCurve = -1
a = [1, 1, 1]
error = 9999
h = 0

#for a parameter a, runs the code of question 3 and 4 to find the length of the curve
while error >= 0.00001:
    l = findLength(a, h)
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