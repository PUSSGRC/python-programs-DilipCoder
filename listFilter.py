# data handling

list_input = [int(x) for x in input("enter the integers for the list").split()]

# filtering the list 

result = list(filter(lambda x: x<5, list_input))

# printing the result

print(result)
