"""https://www.hackerrank.com/challenges/np-linear-algebra/problem"""

import numpy

print(round(numpy.linalg.det(numpy.array([input().split() for _ in range(int(input()))],float)),2))

