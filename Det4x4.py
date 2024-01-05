def minor(matr, k):
    res = []
    for r in matr[1:]:
        row = []
        for j in range(len(r)):
            if j != k:
                row.append(r[j])
        res.append(row)
    return res

def det(matr):
    n = len(matr)
    if n == 2:
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
    s = 0
    z = 1
    for i in range(n):
        #print(det(minor(matr, i)))
        #print(minor(matr, i))
        s += z * matr[0][i] * det(minor(matr, i))
        z = -z
    #print(s)
    return s    


def det4(r0, r1, r2, r3):
    return det([r0, r1, r2, r3])
