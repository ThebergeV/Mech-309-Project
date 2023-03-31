#from Question 4 import *
import numpy as np
import math

minA = -1
maxA = -1
a = 0

#for a parameter a, runs the code of question 3 and 4 to find the length of the curve
while error >= 0.00001:
    l = length(a)
    errorMin = 0
    errorMax = 0
    #Replaces the value of a if it give the minimum length of the curve or the maximum
    if (minA < 0 or l < minA):
        errorMin = abs(minA - l)
        minA = l
        aMin = a
    if (maxA < 0 or l > maxA):
        errorMax = abs(maxA - l)
        maxA = l
        aMax = a
    error = max(errorMin, errorMax)
    a = a + error