import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import math
from fractions import Fraction


def Vector():
    print("Enter values for 3D vector for magnitude")
    x = float(input('Enter X value: '))
    y = float(input('Enter Y value: '))
    z = float(input('Enter Z value: '))
    x = x**2
    y = y**2
    z = z**2
    t = x+y+z
    if t<0: 
        print('ERROR')
    else:
        print(math.sqrt(t))


def Angle():
    print("Enter values for 3D vector A ")
    x = float(input('Enter X value: '))
    y = float(input('Enter Y value: '))
    z = float(input('Enter Z value: '))
    print("Enter values for 3D vector B ")
    t = float(input('Enter X value: '))
    r = float(input('Enter Y value: '))
    e = float(input('Enter Z value: '))
    d = x*t+y*r+z*e
    a = (x**2)+(y**2)+(z**2)
    b = (t**2)+(r**2)+(e**2)
    c = (math.sqrt(a))*(math.sqrt(b))
    g = (math.acos(d/c))
    f = (g*180/math.pi)
    print(f)

calcq = input('Chose calculator type: Vector Magnitude "M" or Angle "A" between 2 vectors ')
if calcq == 'M':
    Vector()
elif calcq == 'm':
    Vector()
elif calcq == 'A':
    Angle()
elif calcq == 'a':
    Angle()
else:
    print('Not an option.')


# p = 1,3,5,3,5,2,6,8,6,8
# q = 1,1,1,2,2,1,2,1,1,1

# plt.bar(p,q)
# plt.show()