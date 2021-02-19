import re

def isNameValid(name):
    if re.search('^[A-Za-z\s]+[A-Za-z]$',name):
        return True
    return False
def isNumValid(mobile):
    if re.search('^[6-9][0-9]{9}$',mobile):
        return True
    return False