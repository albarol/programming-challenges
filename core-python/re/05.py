# Match a street address according to your local format (keep your regex general enough to match any number of street words, including the type designation). For example, American street addresses use the format: 1180 Bordeaux Drive. Make your regex flexible enough to support multi-word street names such as: 3120 De la Cruz Boulevard.

# pattern: Address, number - City - State

import re

def get_complete_address(data):
    return "\r\nAddress: %s - Number: %s - City: %s - State: %s" % (data[0], data[1], data[2], data[3])

addresses = """
rua alves peixoto, 999 - Sao Paulo - SP
rua novato novo, 8157 - Londrina - PR
av alvares camarao, 1 - Palmas - TO
"""

pattern = re.compile("([\w\s]+),\s{1}([0-9]+)\s-\s([\w\s]+)\s-\s([a-zA-Z]{2})")
result = map(lambda address: get_complete_address(address), pattern.findall(addresses))

print "******************"
print "*   ADDRESSES    *"
print "******************"

print "\r\n".join(result)
