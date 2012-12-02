import pickle
import urllib

url = """
http://www.pythonchallenge.com/pc/def/banner.p
"""

content = urllib.urlopen(url).read()
banner = pickle.loads(content)

for row in banner:
    gfx_row = []
    for char, size in row:
        gfx_row.append(char.rjust(size, char))
    print "".join(gfx_row)

# next url: http://www.pythonchallenge.com/pc/def/channel.html
