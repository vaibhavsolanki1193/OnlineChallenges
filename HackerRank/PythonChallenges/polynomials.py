"""https://www.hackerrank.com/challenges/np-polynomials/problem"""

import numpy as np 

A,B = [float(x) for x in input().split()],int(input())
print(np.polyval(A,B))



