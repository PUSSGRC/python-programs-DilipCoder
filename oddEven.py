a = [int(x) for x in input("enter the numbers:").split()]

for x in a:
    if x % 2 ==0:
        print("{} is a even number".format(x))
    else:
        print("{} is a odd number".format(x))
