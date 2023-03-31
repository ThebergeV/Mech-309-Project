#from question 3 import *
import numpy as np
import math

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

#Running the code of question 3, obtains an array of points on the curve
#Curve = subprocess.run(["Points", "Question 3"])
Curve = [[3, 0, 0,], [0, 3, 0], [-3, 0, 0], [14, 0, 0]]

#creates an array that will store the information needed for this program.
#distArray[0] = index of point in the curve array
#distArray[1] = index of one of the 2 closest points to that point
#distArray[2] = distance from target point to closest point 1
#distArray[3] = index of the other one of the 2 closest points to that point
#distArray[2] = distance from target point to closest point 2
distArray = np.empty((0, 5))

#Creates and fills an array of array with the distance information
i = 0
for point in Curve:
    distArray = np.append(distArray, [i, 0, 0, 0, 0])
    distArray.resize((i+1, 5))

    #Calculates the length between the selected point and the other points
    for otherpoints in Curve:
        if otherpoints != point:
            dist = distance(point, otherpoints)
            #If there are slots in the array that have not been used yet, replaces them with the current points and distances
            if min(distArray[i][2], distArray[i][4]) == 0:
                indOfMin = findIndex(distArray[i], min(distArray[i][2], distArray[i][4]))

                distArray[i][indOfMin - 1] = Curve.index(otherpoints)
                distArray[i][indOfMin] = dist

            #If the current point is closer to the target point than the points stored in the array, replaces the furthest one
            elif dist < max(distArray[i][2], distArray[i][4]):
                indOfMax = findIndex(distArray[i], max(distArray[i][2], distArray[i][4]))

                distArray[i][indOfMax - 1] = Curve.index(otherpoints)
                distArray[i][indOfMax] = dist
    i += 1

#Calculates total length of curve
pointsAdded = []
length = 0
loop = "open"
for point in distArray:
    if loop != "closed":
        #Adds every point in the array to the array pointsAdded once their distance from other points have been added to avoid counting them twice
        pointsAdded.append(point[0])
        #for each point, if one of their closest 2 points is not in the pointsAdded array, adds their distance to the lenght total
        if point[1] not in pointsAdded:
            length = length + point[2]
        elif point[3]  not in pointsAdded:
            length = length + point[4]
        #If the 2 closest points are in the pointsAdded array, looks to see if one of the 2 closest points is the starting point (could be a loop curve)
        #If it is a loop, adds the distance to close the loop
        elif point[1] == pointsAdded[0]:
            length = length + point[2]
            loop = "closed"
        elif point[3] == pointsAdded[0]:
            length = length + point[4]
            loop = "closed"

print(length)