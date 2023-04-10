"""

@author: Jeremy
"""

from Question_5 import Newton
import numpy as np


'''''

7. Specify the domain of definition of the length of the intersection curve in terms of parameter a.

To do this we must find the solution to the system of equations at different parameters a. They will be called parameter
b, because a is already being used as a variable. 

The length of the intersection curve is only defined if the intersection curve exists. This means we don't have to evaluate the length,
we can just evaluate the system of equations. They will have the same domain of definition.

Furthermore, we just have to find an initial point a0, using Newton's method. As long as there is a solution to the system of equations
where one point a0 exists, then the intersection curve exists and has a length. 

(Technically there needs to be two points, but if one point exists then two points exist. Our method for finding the intersection 
curve is not precise enough to find the precise location where the functions only intersect at one a single point. It also wouldn't impact
the domain of definition of the function.)

'''

#function outputs the domain
#input range of parameters b and step h

def findDomain(b_min, b_max, h):

    b = b_min
    i = 0

    #init domain of definition

    domain = []  #List that holds the full set of b for which there is a solution
    sub_domain = [] #Holds subsets of continuous b values for which there is a solution
    shortDomain = [] #Ouputs domain in interval notation

    #finds a solution for every value of b

    while b <= b_max:
    
        a = Newton([0,20,b], b)

    
        if np.isnan(a[0]) == False:
            sub_domain.append(b)
    
        else:
        
            if sub_domain != []:
        
                domain.append(sub_domain)

            sub_domain = []
    
        
        b = round(b + h, 3)

    

    if sub_domain != []:
        domain.append(sub_domain)

    #Turn full set of defined b values to interval notation
    for i in range(len(domain)):
        min = np.min(domain[i])
        max = np.max(domain[i])
        shortDomain.append([min,max])

    #Create the message
    
    message = "The domain of definition of the intersection curve length is b = "
    message = message + str(shortDomain[0])
    print(shortDomain)

    #Adds different sets continuous sub-domains of definition into interval notation
    for i in range(1, len(shortDomain)):
        message = message + " U " + str(shortDomain[i])
    
    print(message)

    return domain #Outputs list with full set of solutions

findDomain(-200,200,1)




