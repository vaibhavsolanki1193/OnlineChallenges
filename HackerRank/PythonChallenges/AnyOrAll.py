""" Challenge at https://www.hackerrank.com/challenges/any-or-all/problem"""
n, number = int(input()), list(i for i in input().split())
print((all(float(i) >0 for i in number)) and any(a == a[::-1] for a in number))