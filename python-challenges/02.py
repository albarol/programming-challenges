from string import maketrans 

message = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

instring = "abcdefghijklmnopqrstuvwxyz"
outstring = "cdefghijklmnopqrstuvwxyzab"

translate = maketrans(instring, outstring)

print message.translate(translate)


url = """
http://www.pythonchallenge.com/pc/def/map.html
"""

print url.translate(translate)

# next url: http://www.pythonchallenge.com/pc/def/ocr.html

