# Match simple Web domain names that begin with "www."
# and end with a ".com" suffix; for example, www.yahoo.com. 
# Extra Credit: If your regex also supports other high-level 
# domain names, such as .edu, .net, etc. (for example, 
# www.foothill.edu).


urls = """
http://www.yahoo.com
ftp://archives.yahoo.com
https://www.usp.br
ftp://files.google.com/news/papper
http://news.yahoo.com?date=today
"""

import re


def get_url_pattern(url):
    return "Schema: %s - Host: %s - Path: %s - Querystring: %s" % (url[0], url[1], url[2], url[3])

pattern = re.compile("(ftp|http|https)://([\w\.]+)([\w\/]+)?([\?\w\/\=]+)?")

result = map(lambda uri: get_url_pattern(uri), pattern.findall(urls))

print "\r\n".join(result)