def count_rectangles():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    length = len(lines[0])
    if not all(len(line) == length for line in lines):
        print("Строки имеют различную длину")
        return

    rectangles = 0
    for i in range(length):
        for j in range(len(lines)):
            if lines[j][i] == '#':
                if (j == 0 or lines[j-1][i] == '.') and (i == 0 or lines[j][i-1] == '.'):
                    rectangles += 1

    print(rectangles)

count_rectangles()