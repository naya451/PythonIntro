from decimal import *
getcontext().prec = 10000

a = input().split(',')
x1 = Decimal(a[0])
y1 = Decimal(a[1])
x2 = Decimal(a[2])
y2 = Decimal(a[3])
x3 = Decimal(a[4])
y3 = Decimal(a[5])

print(abs((x2 - x1) * (y3 - y1)  - (x3 - x1) * (y2 - y1) ) / Decimal(2))