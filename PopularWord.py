import sys
d = {}
for s in sys.stdin:
    s = s.replace('\n', '')
    s = s.split(' ')
    #print(s)
    for i in s:
        if (i == ""):
            continue
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
maxv = max(d.values())
y = [x for x in d if (d[x] == maxv)]
if (len(y) == 1):
    print(y[0])
else:
    print("---")