import math
def middle_characters(string):
    x = len(string) / 2
    if x.is_integer():
        return string[int(x)-1:int(x)+1]
    else:
        return string[math.ceil(x)-1]
