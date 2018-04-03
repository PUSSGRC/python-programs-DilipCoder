import fileinput

total = []
count = False
for line in fileinput.input():
    if count:
        total = [total.map(x:x+line.count(chr(i))) for i in range(65,91)]
    else:
        total = [line.count(chr(i)) for i in range(65, 91)]
        count = True

# print(total)
