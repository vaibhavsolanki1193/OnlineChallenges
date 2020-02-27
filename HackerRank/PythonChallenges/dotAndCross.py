'''https://www.hackerrank.com/challenges/np-dot-and-cross/problem'''

import numpy

a=int(input())
arr1=numpy.array([list(map(int,input().split())) for _ in range(a)])

arr2=numpy.array([list(map(int,input().split())) for _ in range(a)])

print(numpy.dot(arr1,arr2))
