# Match the set of the string representations of all Python integers.


numbers = """
1
32
64
any word
bla
git
hat
01293
the
"""


import re

pattern = re.compile("(\d+)")

print pattern.findall(numbers)
