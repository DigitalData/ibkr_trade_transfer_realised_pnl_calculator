import re

# create a function to remove commas from numbers (facepalms)
def remove_commas(txt):
    if type(txt) != str: return txt
    return re.sub(r",", "", txt)