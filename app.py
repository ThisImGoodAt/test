import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import math
from fractions import Fraction


def Magnitude():
    print("Enter values for 3D vector for magnitude")
    x = float(input('X value: '))
    y = float(input('Y value: '))
    z = float(input('Z value: '))
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
    x = float(input('X value: '))
    y = float(input('Y value: '))
    z = float(input('Z value: '))
    print("Enter values for 3D vector B ")
    t = float(input('X value: '))
    r = float(input('Y value: '))
    e = float(input('Z value: '))
    d = x*t+y*r+z*e
    a = (x**2)+(y**2)+(z**2)
    b = (t**2)+(r**2)+(e**2)
    c = (math.sqrt(a))*(math.sqrt(b))
    g = (math.acos(d/c))
    f = (g*180/math.pi)
    h = round(f,1)
    print("Angle between vectors A and B is:", f, "degrees")
    print("Angle to 2 decimal places:", h, "degrees")

calcq = input('Chose calculator type: Vector Magnitude "M" or Angle "A" between 2 vectors ')
if calcq == 'M':
    Magnitude()
elif calcq == 'Magnitude':
    Magnitude()
elif calcq == 'magnitude':
    Magnitude()
elif calcq == 'm':
    Magnitude()
elif calcq == 'A':
    Angle()
elif calcq == 'a':
    Angle()
elif calcq == 'angle':
    Angle()
elif calcq == 'Angle':
    Angle()
else:
    print('Sorry, that was an invalid command!')