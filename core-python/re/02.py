import re

names = """
Aamir Aaron
Abbey Abbie
Abbot Abbott
Abby Abdel
Abdul Abdulkarim
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

pattern = re.compile("[a-zA-Z]+\s[a-zA-Z]+")
result = map(lambda x: "FirstName: " + x.split(" ")[0] + " LastName: " + x.split(" ")[1], pattern.findall(names))


print "\r\n".join(result)
