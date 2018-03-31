# data handling

num = int(input("enter the number to find divisor: "))

# logic
result = []

for x in range(1,num+1):
    if num % x == 0:
        result.append(x)

# printing the result

print(result)
