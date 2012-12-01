def retrieve_data(url):
    import urllib
    page = urllib.urlopen(url).read()
    start_index = page.index("<!--")
    end_index = page.index("-->")
    message = page[start_index:end_index]
    return "".join(message)

import re

url = """
http://www.pythonchallenge.com/pc/def/equality.html
"""

encoded_message = retrieve_data(url)
message = "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", encoded_message))

print message


