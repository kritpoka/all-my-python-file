import numpy as np
import math 

x1,y1 = [int(e) for e in input("Enter x1,y1 :").split()]
x2,y2 = [int(e) for e in input("Enter x2,y2 :").split()]

def calculateDistance(): 
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

print(calculateDistance())
