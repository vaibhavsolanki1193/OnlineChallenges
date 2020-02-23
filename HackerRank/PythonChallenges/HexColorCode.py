"""https://www.hackerrank.com/challenges/hex-color-code/problem"""


import re
N=int(input())

for i in range(0,N):
    s=input()

    x=s.split()

    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        [print(i) for  i in x]

""" This could be solved using non capturing group as well 
reg = (?<!^)(#(?:[\da-f]{3}){1,2})

Explanation: 

"
(?<!^)(#(?:[\da-f]{3}){1,2})
"
gm
Negative Lookbehind (?<!^)
Assert that the Regex below does not match
^ asserts position at start of a line
1st Capturing Group (#(?:[\da-f]{3}){1,2})
# matches the character # literally (case sensitive)
Non-capturing group (?:[\da-f]{3}){1,2}
{1,2} Quantifier — Matches between 1 and 2 times, as many times as possible, giving back as needed (greedy)
Match a single character present in the list below [\da-f]{3}
{3} Quantifier — Matches exactly 3 times
\d matches a digit (equal to [0-9])
a-f a single character in the range between a (index 97) and f (index 102) (case sensitive)
Global pattern flags
g modifier: global. All matches (don't return after first match)
m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)"""