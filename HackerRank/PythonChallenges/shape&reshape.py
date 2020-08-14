import numpy

arr = numpy.array(input().split(), int)
numpy.set_printoptions(legacy='1.13')
print(numpy.reshape(arr, (3,3)))

