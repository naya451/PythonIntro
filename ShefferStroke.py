def sheff(A, B):
    if ((not A) and (not B)):
        return True
    elif (not A):
        return B
    elif (not B):
        return A
    else:
        return False

