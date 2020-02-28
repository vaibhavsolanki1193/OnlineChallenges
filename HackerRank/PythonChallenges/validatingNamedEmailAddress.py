import re

# name, email = 'VIRUS', '<virus!@variable.:p>'

pattern = r'<[^._-][a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$'

for i in range(int(input())):
    name, email = input().split(' ')
    if re.match(pattern, email):
        print(name,email)