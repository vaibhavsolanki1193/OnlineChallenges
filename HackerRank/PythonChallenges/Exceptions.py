# Code
for i in range(int(input())):
    try:
        a,b = map(int,input().split())
        print(int(a//b))
# there is a difference between / and // . / is used for floating point and // for intergers. 
# They have different exception messages
    except Exception as E:
        print("Error Code:",E)