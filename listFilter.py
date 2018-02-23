# data handling

list_input = [int(x) for x in input("enter the integers for the list: ").split()]

max_bound = int(input("enter maximum bound to shortlisting: "))
# filtering the list 

result = list(filter(lambda x: x< max_bound, list_input))

# printing the result

print(result)
