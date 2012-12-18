# Recognize the following strings: “bat,” “bit,” “but,” “hat,” “hit,” or “hut.”

import re

words = """
bat fish bit book keyboard but nose eye building hat try ok address hit ten lol hut
"""

pattern = re.compile("[bhaiu]{2}t")
result = pattern.findall(words)

print " ".join(result)
