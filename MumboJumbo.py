import sys
k = 0
s1 = set()
s2 = set()
for s in sys.stdin:
    if (k == 0):
        s1 = s1.union(set(s))
    else:
        s2 = s2.union(set(s))
    k ^= 1
s1.discard('a')
s1.discard('e')
s1.discard('u')
s1.discard('i')
s1.discard('o')
s1.discard('y')
s2.discard('a')
s2.discard('e')
s2.discard('u')
s2.discard('i')
s2.discard('o')
s2.discard('y')
if (len(s1) > len(s2)):
    print("Mumbo")
else:
    print("Jumbo")