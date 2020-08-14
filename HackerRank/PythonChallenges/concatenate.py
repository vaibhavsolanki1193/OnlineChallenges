"""https://www.hackerrank.com/challenges/np-concatenate/problem"""

import numpy


n, m , p = map(int, input().split())

arrN = numpy.array([input().split() for _ in range(n)],int)
arrM = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((arrN, arrM), axis=0))
