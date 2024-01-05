
def are_equal(s1, s2):

    for i in range(len(s2)):
        if (s1[i] != s2[i] and s2[i] != '@'):
            return False
    return True

s1 = input()
s2 = input()
m = 0
n = s2.find('@')
k = -1
ind = 0
ind = s1.find(s2[m:n], ind)
while  ind != -1:
    #print(s1.find(s2[m:n]))
    if (k == -1):
        k = ind
    #print(s1[ind:ind + len(s2)], s2)
    if (ind + len(s2) <= len(s1) and are_equal(s1[ind:ind + len(s2)], s2)):
        break
    k = -1
    ind = s1.find(s2[m:n], ind + 1)
    
print(k)

