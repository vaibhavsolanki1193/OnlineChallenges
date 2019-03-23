# problem on https://www.hackerrank.com/challenges/find-angle/problem

import math 
AB, BC = int(input()), int(input()) 
print(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')