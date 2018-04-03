# Data handling 
try:
    num = int ( input ('Enter the number: \n'))
except TypeError:
    print('Enter the numbers  value only')

result = sum(x*x for x in range(1, num+1, 2))


print(result)
