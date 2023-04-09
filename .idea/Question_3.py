# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 14:10:57 2023

@author: Anika
"""

'''
equations:
    S1 = X^4 + sin(Y) + Z^4 = 0
    S2 = X^3 + e^Y + (Z-4)^3 = 0
    
Question 3: provide the equations to be satisfied
by the intersection curve. Implement Python-only 
procedure able to generate a 3D plot showing the
intersection curve. In the same plot, showing
the chosen surface functions is welcome but not
mandatory.
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
    
def S1(x,y,z): #implicit function = 0
    return x**4 + np.sin(y) + z**4

def S2(x,y,z): #implicit function = 0
    return x**3 + np.e**y + (z-4)**3


#Jacobian
def Jacobian(x, y, z):
    return np.array([[4*x**3, np.cos(y), 4*z**3], [3*x**2, np.e**y, 3*(z-4)**2]])

#Newton's method to find intersect point
def Newton(a):
    eps = 1e-3
    norm = 1
    while norm > eps:
        inv = np.linalg.pinv(Jacobian(a[0], a[1], a[2]))
        h = np.dot(inv, [-S1(a[0], a[1], a[2]), -S2(a[0], a[1], a[2])])
        a = a + h
        norm = np.linalg.norm(h)
        
    return a

#initial point
a0 = Newton([1,1,1])
intersect = []
intersect.append(np.copy(a0)) #list of numpy arrays

#tracing
def trace(a, h):
    #initial 2nd point
    a1 = Newton(np.add(a, [h/3, h/3, h/3]))
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
        a = Newton(a)
        intersect.append(np.copy(a))
        n = n + 1 
        if n > 2000:
            print("diverged")
            break
 
    return intersect

#list of points on interesction curve
points = trace(a0, 0.01)

def plotCurve(points, bbox=(-10,10)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
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

plotCurve(points)