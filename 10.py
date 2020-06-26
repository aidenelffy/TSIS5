import re
def text_match(text):
        patterns = '\w+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("Ashg ugku"))
print(text_match("7 bkbk"))
print(text_match(" ! hjk"))