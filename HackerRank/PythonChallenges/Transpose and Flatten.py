# problem on https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?h_r=next-challenge&h_v=zen
import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())
