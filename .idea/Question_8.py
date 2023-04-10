from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from Question_7 import *
from Question_5 import *
from PIL import Image


#Plots the intersection curve. Similar to the one in question 5, but modified slightly to create the animation
def plotCurve2(points, bbox=(-10,10)):

    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(-5,5) #set fixed axes to see the curve motion
    ax.set_ylim(0,10)
    ax.set_zlim(-5,10)

    ax.set_xlabel("X axis") #Axis labels
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")

    A = np.linspace(xmin, xmax, 100) # resolution of the contour
    B = np.linspace(xmin, xmax, 15) # number of slices
    A1,A2 = np.meshgrid(A,A) # grid on which the contour is plotted

    for i in range(len(points)):
        end = points[i]
        if i == 0:
            start = points[i]
            
        else:
            ax.plot([start[0], end[0]], [start[1], end[1]], zs=[start[2], end[2]], c="b")
    
            start = end
        

# creates animation of the intersection curve
def createAnim(bmin, bmax, h):

    fullbVals = findDomain(bmin,bmax,h) #Returns list b values
    bvals = fullbVals[0]
    n = len(bvals) #Number of individual b values

    for j in range(n): #Saves n images of a plot of the intersectino curve with parameter b
        b = bvals[j]
        points = trace([1,1,1], 0.01, b)
        plotCurve2(points)
        plt.title("Intersection curve for b = " + str(b)) #Plot title
        plt.savefig(f"{j}.png") #Saves plot image
        plt.close() #Closes plot


    images = [Image.open(f"{n}.png") for n in range(n)] #Opens all of the images that were just created

    images[0].save('animation.gif', save_all=True, append_images=images[1:], duration=100, loop=0) ##Combines images of the plot into a .gif file to animate the plot

createAnim(-6,10,0.1)

