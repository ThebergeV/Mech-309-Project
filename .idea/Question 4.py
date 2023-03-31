#from question 3 import *
import numpy as np
import math

def distance(point1, point2):
    dist = math.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
    return dist
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


#Curve = subprocess.run(["Points", "Question 3"])
Curve = [[3, 0, 0,], [0, 3, 0], [-3, 0, 0], [-4, 0, 0]]

distArray = np.empty((0, 5))

i = 0
for point in Curve:
    distArray = np.append(distArray, [i, 0, 0, 0, 0])
    distArray.resize((i+1, 5))
    for otherpoints in Curve:
        if otherpoints != point:
            dist = distance(point, otherpoints)

            if min(distArray[i][2], distArray[i][4]) == 0:
                indOfMin = findIndex(distArray[i], min(distArray[i][2], distArray[i][4]))

                distArray[i][indOfMin - 1] = Curve.index(otherpoints)
                distArray[i][indOfMin] = dist
            elif dist < max(distArray[i][2], distArray[i][4]):
                indOfMax = findIndex(distArray[i], max(distArray[i][2], distArray[i][4]))

                distArray[i][indOfMax - 1] = Curve.index(otherpoints)
                distArray[i][indOfMax] = dist
    i += 1

prev = -1
pointsAdded = []
length = 0
for point in distArray:
    pointsAdded.append(point[0])
    print("point:")
    print(point)
    print("pointsAdded:")
    print(pointsAdded)
    if point[1] not in pointsAdded:
        length = length + point[2]
    elif point[3]  not in pointsAdded:
        length = length + point[4]
    elif point[1] == pointsAdded[0]:
        length = length + point[2]
    elif point[3] == pointsAdded[0]:
        length = length + point[4]

print(length)