import random

def divrandom(a, b, s, p):
    if b < a:
        tmp = a 
        a = b
        b = tmp
    x = True
    i = 0
    while x:
        i += 1
        n3 = random.randrange((b - a) // s + 1)
        if (a + n3 * s) % p != 0:
            return a + n3 * s
        if (i > 100):
            return 0

