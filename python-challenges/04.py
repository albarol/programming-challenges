def retrieve_data(url):
    import urllib
    return urllib.urlopen(url).read()

def retrieve_next_link(info):
    import re
    pattern = re.compile("[0-9]{4,5}")
    return "".join(pattern.findall(info))

next_url = """
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={id}
"""
next_link = 0

for i in range(400):
    info = retrieve_data(next_url.format(id=next_link))
    next_link = retrieve_next_link(info)
    print info


# next url: http://www.pythonchallenge.com/pc/def/peak.html