# https://www.hackerrank.com/challenges/re-split/problem
regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# Case that handles two consecutive delimiters 
r"""
import re
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')
filter() returns every element in the second argument for which the function in the first argument evaluates as true.
 Using None as the first argument removes all items that are equivalent to false. The latter two test cases have 
 consecutive delimiters, so using re.split() creates empty elements in the list. filter() returns the list without those 
 empty elements.
"""