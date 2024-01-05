def factorize(start, n):
    i = start
    primfac = []
    while i * i <= n:
        if n % i == 0:
            k = factorize(i, n // i)
            for p in k:
                primfac.append([i] + p)
        
        i = i + 1
    if n > 1:
        primfac.append([n])
    return primfac

number = int(input())
for i in factorize(2, number):
    for k in i[:len(i) - 1:]:
        print(k, end="*")
    print(i[len(i) - 1])