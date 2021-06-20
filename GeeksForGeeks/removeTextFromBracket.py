instring = "(Text) to be (deleted)"

import re

patt = re.sub(r"\(.*?\)",'(.)', instring)

print(patt)