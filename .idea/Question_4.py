import numpy as np
import math
from Question_3 import *

def findLength(a, h):
    Curve = trace(a, h)
    curve1 = np.empty((1, 3))
    j = 0
    for points in Curve:
        curve1 = np.append([curve1], [points])
        curve1.resize((j+2, 3))
        j = j+1

    size0 = curve1.size
    length0 = (size0 - 1) * h
    error = 99999
    h1 = h
    while error >= 0.001:
        Curve = trace(a, h1)
        curve2 = np.empty((1, 3))
        j = 0
        for points in Curve:
            curve2 = np.append([curve2], [points])
            curve2.resize((j+2, 3))
            j = j+1

        size = curve2.size
        length = (size - 1) * h1
        error = abs(length - length0)
        length0 = length
        h1 = h1/2
        print("length: " + str(length))
        print("error: " + str(error))
        print("h: " + str(h1))
        print("number of point:" + str(size))