"""

@author: Vincent
"""


import numpy as np
import math
from Question_5 import *

#function measuring the distance between 2 points
def distance(point1, point2):
    dist = math.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
    return dist
def newCurve(a, h, b):
    Curve = trace(a, h, b)
    return Curve

def findLength(a, h, b):

    Curve = newCurve(a, h, b)
    pointsAdded = []
    length = 0
    #Creates and fills an array of array with the distance information
    i = 0
    z = 0
    firstNonNan = -1
    for point in Curve:
        if (str(point[0]) != "nan"):
            distmin1 = 99999
            distmin2 = 99999
            if firstNonNan == -1:
                firstNonNan = i

            duplicate = False
            for duplicates in pointsAdded:
                if (distance(point, duplicates) == 0):
                    duplicate = True


            if (i < Curve.__len__()-1 and duplicate == False):
                if(str(Curve[i+1][0]) != "nan"):
                    dist = distance(point, Curve[i+1])
                    length += dist
                    z += 1
                    pointsAdded = np.append(pointsAdded, point)
                    pointsAdded.resize((z,3))
            else:
                for otherPoints in Curve:
                    distStart = distance(point, Curve[i])
                    dist = distance(point, otherPoints)
                    if (dist < distmin1):
                        distmin1 = dist
                    elif (dist <= distmin2):
                        distmin2 = dist
                    if distStart <= distmin1 or distStart <= distmin2:
                        length += distStart
        i += 1




    return length