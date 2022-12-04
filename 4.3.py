'''Write a program which accepts a sequence of comma-separated numbers 
console and output them in list and tuple form.'''

entered_numbers = input("Enter your numbers: ")
list_numbers = entered_numbers.split(",") #for List
tuple_numbers = tuple(list_numbers) #for tuple
print(list_numbers)
print(tuple_numbers)