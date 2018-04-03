# Data Handling

try:
    numList = [int(x) for x in input('Enter the numbers: \n').split()]
except TypeError:
    print('enter the numeric values only')

# logic to fin max and min value


def minMax(values):
    min, max = values[0], 0
    for i in values:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

print(minMax(numList))
