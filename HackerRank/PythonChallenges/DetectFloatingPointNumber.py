# https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re 
for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', input())))


Regex_note=r"""
^[+-]?[0-9]*\.[0-9]+$
"
gm
^ asserts position at start of a line
Match a single character present in the list below [+-]?
? Quantifier — Matches between zero and one times, as many times as possible, giving back as needed (greedy)
+- matches a single character in the list +- (case sensitive)
Match a single character present in the list below [0-9]*
* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
0-9 a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
\. matches the character . literally (case sensitive)
Match a single character present in the list below [0-9]+
+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
0-9 a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
$ asserts position at the end of a line
Global pattern flags
g modifier: global. All matches (don't return after first match)
m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
"""