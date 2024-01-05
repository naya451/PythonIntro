import itertools
def look_and_say1(number='1'):
    while True:
        yield number
        number = ''.join(str(len(list(g))) + k for k, g in itertools.groupby(number))

def LookSay():
    a = look_and_say1()
    while (1):
        b = next(a)
        for i in b:
            yield int(i)
