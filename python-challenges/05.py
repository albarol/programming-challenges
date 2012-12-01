import pickle
import urllib

url = """
http://www.pythonchallenge.com/pc/def/banner.p
"""

content = urllib.urlopen(url).read()
banner = pickle.loads(content)

gfx = []

for row in banner:
    gfx_row = []
    for char, size in row:
        gfx_row.append(char.rjust(size, char))
    gfx.append("".join(gfx_row))

for line in gfx:
    print row

# next url: http://www.pythonchallenge.com/pc/def/channel.html
