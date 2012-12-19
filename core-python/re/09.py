# Match the set of the string representations of all Python floats.

numbers = """
1.1
23.4
any word
bla
git
hat
0.00000000001
the 
"""


import re

pattern = re.compile("([0-9\.]+)")

print pattern.findall(numbers)
