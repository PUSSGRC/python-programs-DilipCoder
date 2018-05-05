#data handling
n = int(input())
strings = []
for i in range(n):
    inputs = input()
    strings.append(inputs)

# print(strings)
# logic
def fibbonaci(a, b, c):
    if (a==b+c) or (b == a+b) or (c == a+b):
        return True
    else:
        return False

for string in strings:
    completed = []
    last = len(string)
    count = [0] * last
    k = 0
    for i in range(last):
        if string[i] in completed:
            continue
        else:
            completed.append(string[i]) 
            for j in range(i,last):
                if string[i] == string[j]:
                    count[k]+=1
            k +=1
    test = False
    constraint = len(completed)
    if constraint >= 3 :
        for i in range(2, constraint):
            test = fibbonaci(count[i], count[i-1],count[i-2])
            if test:
                print("Dynamic")
                break;
        if not test:
            print("Not")
    else:
        print("Not")
