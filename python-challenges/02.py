url = "http://www.pythonchallenge.com/pc/def/ocr.html"

def recovery_information(url):
    import urllib    
    page = urllib.urlopen(url).read()
    message = page[page.index("%"):]
    return "".join(message)

import re

ocr = recovery_information(url)
pattern = re.compile("[a-zA-Z]+")
message =  pattern.findall(ocr)
print "".join(message)

# next url: http://www.pythonchallenge.com/pc/def/equality.html
