import re
def text_match(text):
        patterns = 'a.*b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab_vv"))
print(text_match("aaaabbbbbb"))
print(text_match("Add_ccA"))