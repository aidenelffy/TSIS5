"""import re

text = "Azaz ghjk n"
pattern = "z"
match = re.findall(pattern, text)
print(match())
"""
import re
def text_match(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

text = str(input())
print(text_match(text))
