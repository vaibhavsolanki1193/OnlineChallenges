instring = "This[ is the{} main text ] )file ("

import re 

pat = re.sub(r"[\[\{}\])(]","", instring)

# print(pat)
with open('../temp/output.txt', 'w') as fw:
    fw.write(pat)
    print(pat)
    print("added to file")