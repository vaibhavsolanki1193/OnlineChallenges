
"""https://www.hackerrank.com/challenges/re-findall-re-finditer/problem"""

import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))


"""
“lookaround”
Lookahead and lookbehind, collectively called “lookaround”, are zero-length assertions just like the start and end of line, and start and end of word anchors explained earlier in this tutorial. The difference is that lookaround actually matches characters, but then gives up the match, returning only the result: match or no match. That is why they are called “assertions”. They do not consume characters in the string, but only assert whether a match is possible or not. Lookaround allows you to create regular expressions that are impossible to create without them, or that would get very longwinded without them.
Positive and Negative Lookahead
Negative lookahead is indispensable if you want to match something not followed by something else. When explaining character classes, this tutorial explained why you cannot use a negated character class to match a q not followed by a u. Negative lookahead provides the solution: q(?!u). The negative lookahead construct is the pair of parentheses, with the opening parenthesis followed by a question mark and an exclamation point. Inside the lookahead, we have the trivial regex u.

Positive lookahead works just the same. q(?=u) matches a q that is followed by a u, without making the u part of the match. The positive lookahead construct is a pair of parentheses, with the opening parenthesis followed by a question mark and an equals sign.

You can use any regular expression inside the lookahead (but not lookbehind, as explained below). Any valid regular expression can be used inside the lookahead. If it contains capturing groups then those groups will capture as normal and backreferences to them will work normally, even outside the lookahead. (The only exception is Tcl, which treats all groups inside lookahead as non-capturing.) The lookahead itself is not a capturing group. It is not included in the count towards numbering the backreferences. If you want to store the match of the regex inside a lookahead, you have to put capturing parentheses around the regex inside the lookahead, like this: (?=(regex)). The other way around will not work, because the lookahead will already have discarded the regex match by the time the capturing group is to store its match.

Positive and Negative Lookbehind
Lookbehind has the same effect, but works backwards. It tells the regex engine to temporarily step backwards in the string, to check if the text inside the lookbehind can be matched there. (?<!a)b matches a “b” that is not preceded by an “a”, using negative lookbehind. It doesn’t match cab, but matches the b (and only the b) in bed or debt. (?<=a)b (positive lookbehind) matches the b (and only the b) in cab, but does not match bed or debt.

The construct for positive lookbehind is (?<=text): a pair of parentheses, with the opening parenthesis followed by a question mark, “less than” symbol, and an equals sign. Negative lookbehind is written as (?<!text), using an exclamation point instead of an equals sign.
"""