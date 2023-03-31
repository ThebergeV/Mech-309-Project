#from Question 4 import *
import numpy as np
import math

minCurve = -1
maxCurve = -1
a = 0

#for a parameter a, runs the code of question 3 and 4 to find the length of the curve
while error >= 0.00001:
    l = length(a)
    errorMin = 0
    errorMax = 0
    #Replaces the value of a if it give the minimum length of the curve or the maximum
    if (minCurve < 0 or l < minCurve):
        errorMin = abs(minCurve - l)
        minCurve = l
        aMin = a
    if (maxCurve < 0 or l > maxCurve):
        errorMax = abs(maxCurve - l)
        maxCurve = l
        aMax = a
    error = max(errorMin, errorMax)
    a = a + error