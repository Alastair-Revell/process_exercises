# i-vector, j-vector

def check_walk(array):

    if array.count('n') == array.count('s') and array.count('e') == array.count('w') and len(array) == 10:
        return True
    else:
        return False
