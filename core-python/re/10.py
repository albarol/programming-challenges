# Match the set of the string representations of all Python complex numbers.

numbers = """
1.1j
23.4
any word
bla
git
hat
1j
234j
1j
the 
"""


import re

pattern = re.compile("([0-9\.]+)j")

print pattern.findall(numbers)
