import re
def text_match(text):
        patterns = '^[_0-9a-zA-Z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

text = str(input())
print(text_match(text))