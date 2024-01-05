width, height = [int(i) for i in input().split(',')]
result = A = [ [0]*width for i in range(height) ]
count = 0
for n in range(width + height):
    for i in range(n+1):
        if n % 2 == 0:
            if i >= height or (n - i) >= width: 
                continue
            result[i][n - i] = str(count % 10)
        else:
            if (n - i) >= height or i >= width:
                continue
            result[n - i][i] = str(count % 10)
        count += 1

print('\n'.join([' '.join(e) for e in result]))