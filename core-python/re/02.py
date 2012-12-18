# Match any pair of words separated by a single space, that is, first and last names.

import re

names = """
Aamir Aaron
Abbey, Abbie
Abbot, Abbott
Abby, Abdel
Abdul, Abdulkarim
Abdullah Abe
Abel Abelard
Abner Abraham
Abram Ace
Adair Adam
Adams Addie
Adger Aditya
Adlai Adnan
Adolf Adolfo
Adolph Adolphe
Adolpho Adolphus
Adrian Adrick
Adrien Agamemnon
Aguinaldo Agamemnon
"""

def get_complete_name(name):
    complete_name = name.split(" ")
    return "First: %s - Last: %s" % (complete_name[0], complete_name[1])

pattern = re.compile("[a-zA-Z]+\s[a-zA-Z]+\n")
result = map(lambda x: get_complete_name(x), pattern.findall(names))

print "******************"
print "*     NAMES      *"
print "******************"

print "\r".join(result)
