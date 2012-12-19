# Match the set of the string representations of all Python longs.


numbers = """
1L
0xFFFFFFFF
any word
bla
git
hat
4294967295L
the 
"""


import re

pattern = re.compile("([0-9A-FLx]+)")

print pattern.findall(numbers)
