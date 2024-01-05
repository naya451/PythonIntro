import sys

#count = 0
#candidate = None
#for element in sys.stdin:
#    if count == 0:
#        candidate = element
#    count += 1 if element == candidate else -1
#print(candidate)


count = 0
candidate = None
for element in sys.stdin:
    if (element == "" or element == '\n'):
        continue
    element = eval(element)
    if count == 0:
        candidate = element
    count += 1 if element == candidate else -1
print(candidate)

