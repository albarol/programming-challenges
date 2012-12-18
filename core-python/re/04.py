# Match the set of all valid Python identifiers.

import re

source_code = """
import re

def get_complete_name(name):
    return "First: %s - Last: %s" % (name[1], name[0])

pattern = re.compile("([a-zA-Z]+),\s+([a-zA-Z]+)")

print "******************"
print "*     NAMES      *"
print "******************"

result = map(lambda name: get_complete_name(name), pattern.findall(names))

print "\r\n".join(result)
"""

identifiers = ['import', 'def', 'print', 'map', 'if', 'while', 'for']

print [i for i in identifiers if i in source_code]

