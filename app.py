import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import math

# print(np.pi)

print("Enter Values from 3D vector for magnitude")
x = float(input('Enter X value: '))
y = float(input('Enter Y value: '))
z = float(input('Enter Z value: '))
x = x**2
y = y**2
z = z**2
t = x+y+z
print(math.sqrt(t))


# p = 1,3,5,3,5,2,6,8,6,8
# q = 1,1,1,2,2,1,2,1,1,1

# plt.bar(p,q)
# plt.show()