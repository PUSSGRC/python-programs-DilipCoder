# data handling
n = input('Enter the number: \n')
num = int(n)

def sumOfSquare(num):
    if num == 1:
        return 1
    else:
        return sumOfSquare(num-1) + num*num

result = sumOfSquare(num)

print(result)
