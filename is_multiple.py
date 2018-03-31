# data handling
n,m = (int(x) for x in  input("Enter the two number, n to check multiple of m:\n").split( ))
def is_multiple(n, m):
    if(n % m == 0):
        return True
    else:
        return False

print(is_multiple(n, m))
