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

#function finding the index of the target value in the array
def findIndex(array, value):
    i = 0
    for val in array:
        if i == 2:
            if val == value:
                return i
        elif i == 4:
            if val == value:
                return i
        i = i+1

def findLength(a, h, b):
    l0 = findLengthMethod(a, h, b)
    error0 = 10
    error = error0
    h0 = h
    while error>= 0.1:
        l1 = findLengthMethod(a, h0, b)
        error = abs(l1 - l0)
        l0 = l1
        h0 = h0/2
    return l0

def findLengthMethod(a, h, b):
    Curve = trace(a, h, b)
    curve2 = np.empty((1, 3))
    j = 0
    for points in Curve:
        curve2 = np.append([curve2], [points])
        curve2.resize((j+2, 3))
        j = j+1

    #creates an array that will store the information needed for this program.
    #distArray[0] = index of point in the curve array
    #distArray[1] = index of one of the 2 closest points to that point
    #distArray[2] = distance from target point to closest point 1
    #distArray[3] = index of the other one of the 2 closest points to that point
    #distArray[2] = distance from target point to closest point 2
    distArray = np.empty((0, 5))
    pointsAdded = []
    length = 0
    loop = "open"
    #Creates and fills an array of array with the distance information
    i = 0
    for point in curve2:
        distmin1 = 99999
        minInd1 = -1
        distmin2 = 99999
        minInd2 = -1
        z = 0
        #Calculates the length between the selected point and the other points
        for otherpoints in curve2:
            if otherpoints[0] != point[0] or otherpoints[1] != point[1] or otherpoints[2] != point[2]:
                dist = distance(point, otherpoints)

                #If the current point is closer to the target point than the current closest points replaces the furthest one
                if dist < max(distmin1, distmin2):

                    if(distmin1 >= distmin2):
                        distmin1 = dist
                        minInd1 = z

                    else:
                        distmin2 = dist
                        minInd2 = z
            z += 1

        #Calculates total length of curve
        if loop != "closed":
            #Adds every point in the array to the array pointsAdded once their distance from other points have been added to avoid counting them twice
            pointsAdded.append(i)
            #for each point, if one of their closest 2 points is not in the pointsAdded array, adds their distance to the lenght total
            if minInd1 not in pointsAdded:
                length = length + distmin1
            elif minInd2  not in pointsAdded:
                length = length + distmin2
            #If the 2 closest points are in the pointsAdded array, looks to see if one of the 2 closest points is the starting point (could be a loop curve)
            #If it is a loop, adds the distance to close the loop
            elif minInd1 == pointsAdded[0]:
                length = length + distmin1
                loop = "closed"
            elif minInd2 == pointsAdded[0]:
                length = length + distmin2
                loop = "closed"
        i += 1


    return length