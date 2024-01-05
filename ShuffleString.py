
def check(s1, s2, k):
    tmp = ""
    for i in range(0, k):
        tmp += s1[i::k]
        #print(tmp)
    return s2 == tmp

s1 = input()
s2 = input()

if (len(s1) == len(s2)):
    indices = []
    ind = -1
    while 1:
        ind = s1.find(s2[1], ind + 1)
        #print(ind)
        if (ind == -1):
            break
        indices.append(ind)
    if indices:
        a = 1
        for k in indices:
            if check(s1, s2, k):
                a = 0
                print(k)
                break
        if a:
            print("No")
    else: 
        print("No")
else:
    print("No")