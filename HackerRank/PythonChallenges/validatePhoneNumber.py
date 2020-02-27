'''https://www.hackerrank.com/challenges/validating-the-phone-number/problem'''

import re 

for i in range(int(input())):
    print('YES' if re.match(r'^[789]\d{9}$', input()) else 'NO')