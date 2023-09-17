#Drempel

import numpy as np

def drempel(x, a, b):
    return (np.clip(x-a, 0, None))/b

drempel(2, 3, 0.25)
drempel(np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]), 1, 2)

#Groepsindeling

import numpy as np

def groepen(l):
    s = []
    for i in range(max(l)+1):
        s.append(np.where(l == i)[0])
    return s

groepen(np.array([0, 1, 0, 2, 1, 0, 2]))
groepen(np.array([0, 2, 0, 2, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 2, 2, 2, 0, 0, 1]))

#Interval

import numpy as np

def I(x, a, b):
    return 

I(np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]), -2, 3)

#Stuksgewijs Constant