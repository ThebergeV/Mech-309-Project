from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


#Same code as for question 3, but with the added parameter b

def S1(x,y,z,b): #implicit function = 0
    return x**4 + np.sin(y) + (z - b)**4

def S2(x,y,z,b): #implicit function = 0
    return (x-b)**3 + np.e**y + (z-4)**3

#Jacobian
def Jacobian(x, y, z, b):
    return np.array([[4*x**3, np.cos(y), 4*(z-b)**3], [3*(x-b)**2, np.e**y, 3*(z-4)**2]])

#Newton's method to find intersect point
def Newton(a, b):
    eps = 1e-3
    norm = 1
    i = 0
    while norm > eps:
        i += 1
        inv = np.linalg.pinv(Jacobian(a[0], a[1], a[2], b))
        h = np.dot(inv, [-S1(a[0], a[1], a[2], b), -S2(a[0], a[1], a[2], b)])
        a = a + h
        norm = np.linalg.norm(h)

        if np.isnan(a[0]) == True:    #Stops the loop if there is no solution
            break
        if i > 2500:                  #Counter to stop loop after too many iterations
            a[0] = float("nan")       #Doesn't converge, therefore there is no solutions
            a[1] = float("nan")       #Assigns NaN to the coordinates when there is no solution. Used in Question 7 when finding the domain of definition
            a[2] = float("nan")
            break

    
    return a


#tracing
def trace(a, h, b):
    #initial point
    a0 = Newton(a,b)
    intersect = []
    intersect.append(np.copy(a0)) #list of numpy arrays
    
    #initial 2nd point
    a1 = Newton(np.add(a, [h/3, h/3, h/3]), b)
    intersect.append(np.copy(a1))
    a = np.copy(a1)
    n = 0
    while(n < 10 or (np.linalg.norm(np.add(a1,-intersect[n])) >= h/2) and (np.linalg.norm(np.add(a0,-intersect[n])) >= h/2)):
        #trace direction
        dirn = (np.add(a, -intersect[n]))/h
        norm = np.linalg.norm(dirn)
        dirn = dirn/norm
        #move h in trace direction
        dirn = dirn*h
        a = np.add(a, dirn)
        a = Newton(a,b)
        intersect.append(np.copy(a))
        n = n + 1 
        if n > 2000:
            print("diverged")
            break
 
    return intersect


#list of points on interesction curve


def plotCurve(points, bbox=(-10,10)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel("X axis")
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
            ax.plot([start[0], end[0]], [start[1], end[1]], zs=[start[2], end[2]])
            start = end
    
    
    plt.show()



