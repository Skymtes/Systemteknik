"""
    This file is used for testing the Blending.py file.
"""

import sys, os, unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Makes file be able to find 'Algorithm Module'
from Algorithm.Blending import Blend

for i in range(0, 51):
 
    for j in range(0, 51):

        print(i, j, Blend(i/100, j/100, 200))

for i in range(0, 101):

    print(i, Blend(0.32, 0, 200, i/100, 0, 50))

# print(Blend(0.32, 0, 200, .80, 0, 37.3))