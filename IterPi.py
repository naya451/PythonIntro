def PiGen():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    three = False
    while True:
        if 4*q+r-t < n*t:
            if three:
                yield str(n)
            else:
                yield str(n)
                three = True
                yield "."
            q, r, t, k, n, l = 10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t-10*n, l
        else:
            q, r, t, k, n, l = q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2

