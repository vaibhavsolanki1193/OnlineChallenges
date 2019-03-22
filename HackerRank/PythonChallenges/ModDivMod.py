# Problem on https://www.hackerrank.com/challenges/python-mod-divmod/problem 
num1, num2 = int(input()), int(input())
print('{0}\n{1}\n({0}, {1})'.format(*divmod(num1,num2)))