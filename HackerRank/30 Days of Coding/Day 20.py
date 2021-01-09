#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def bubble_sort(a):
    n = len(a)
    flag = 0 
    
    for i in range(n-1):
        
        for j in range(n-1):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                flag +=1
        if flag == 0:
            break
    print("Array is sorted in {0} swaps.".format(flag))
    return a
res = bubble_sort(a)
print("First Element: {0}".format(a[0]))
print("Last Element: {0}".format(a[-1]))