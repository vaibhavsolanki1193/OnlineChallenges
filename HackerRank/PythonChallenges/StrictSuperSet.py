# problem at https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(input().split())
for i in range(0, int(input())):
    if not A.issuperset(set(input().split())):
        mark = False
        break
    else:
        mark = True
print(mark)