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

need to parametrize equations
Newton's method to solve?
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def plot_implicit(fn, bbox=(-10,10)):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 100) # resolution of the contour
    B = np.linspace(xmin, xmax, 15) # number of slices
    A1,A2 = np.meshgrid(A,A) # grid on which the contour is plotted

    for z in B: # plot contours in the XY plane
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z')
        # [z] defines the only level to plot for this contour for this value of z

    for y in B: # plot contours in the XZ plane
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y')

    for x in B: # plot contours in the YZ plane
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x')

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)

    plt.show()
    
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
    for n in range(20):
        x = a[0]
        y = a[1]
        z = a[2]
        #trace direction
        dirn = [(4*x**3)*(3*x**2), (np.cos(y))*(np.e**y), (4*z**3)*(3*(z-4)**2)]
        norm = np.linalg.norm(dirn)
        dirn = dirn/norm
        #move h in trace direction
        dirn = dirn*h
        for i in range(3):
            a[i] = a[i] + dirn[i]
        #find intersect point
        a = Newton(a)
        intersect.append(np.copy(a))
    return intersect
trace(a0, 1)

#loop until reaching starting point

#current problem: tracing loop converges, why???