# Problem on https://www.hackerrank.com/challenges/polar-coordinates/problem 

import cmath
import math
number = complex(input())
print(math.sqrt((number.real * number.real) + (number.imag * number.imag)))
print(cmath.phase(number))

# another cool way 
"""
from cmath import polar
print ('{}\n{}'.format(*polar(complex(input()))))
"""