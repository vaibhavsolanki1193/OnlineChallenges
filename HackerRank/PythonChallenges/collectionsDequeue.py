#problem on https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
deq = deque()
for _ in range(0,int(input())):
    action , *elem = input().split()
    getattr(deq, action)(*elem)
    print(*deq)