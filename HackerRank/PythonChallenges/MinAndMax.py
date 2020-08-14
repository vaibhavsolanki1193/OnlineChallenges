"""https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true"""

import numpy

# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])


N, M = map(int, input().split())

my_array = numpy.array([input().split() for _ in range(N)], int)
print(max(numpy.max(my_array, axis=1)))