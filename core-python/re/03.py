# Match any word and single letter separated by a comma and single space, as in last name, first initial

import re

def get_complete_name(name):
    return "First: %s - Last: %s" % (name[1], name[0])


names = """
Aamir, Aaron
Abbey Abbie
Abbot, Abbott
Abby Abdel
Abdul, Abdulkarim
Abdullah, Abe
Abel Abelard
Abner, Abraham
Abram, Ace
Adair, Adam
Adams, Addie
Adger, Aditya
Adlai, Adnan
Adolf, Adolfo
Adolph, Adolphe
Adolpho, Adolphus
Adrian, Adrick
Adrien, Agamemnon
Aguinaldo, Agamemnon
"""

pattern = re.compile("([a-zA-Z]+),\s+([a-zA-Z]+)")


print "******************"
print "*     NAMES      *"
print "******************"

result = map(lambda name: get_complete_name(name), pattern.findall(names))

print "\r\n".join(result)
