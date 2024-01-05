a = input()
a = a.replace(")", "")
a = a.replace("(", "")
a = [int(c) for c in a.split(",")]
a1 = [(i, 1) for i in a[0::2]]
a2 = [(i, 2) for i in a[1::2]]
a = a1 + a2
a = sorted(a, key = lambda x : x[0])
res = 0
c = 0
for i in range(len(a)):
    if c and i:
        res += a[i][0] - a[i-1][0]
    if (a[i][1] == 2):
        c += 1
    else: c -= 1
    
print(res)