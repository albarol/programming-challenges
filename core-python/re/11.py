# Match the set of all valid e-mail addresses (start with a loose 
# regex, and then try to tighten it as much as you can, yet 
# maintain correct functionality).

emails = """
re@re.com.br
python-delivery@python.org
invalid_mail.com
https://www.python.org
"""

import re

pattern = re.compile("[\w\-]+@[\w\-\.]+")

print pattern.findall(emails)
