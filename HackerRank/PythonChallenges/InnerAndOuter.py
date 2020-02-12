import numpy as np
 
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(np.inner(A,B), np.outer(A,B), sep='\n')
