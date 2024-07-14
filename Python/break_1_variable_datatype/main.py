## variables
# variable name must start with a letter or underscore
# variable names are case-sensitive

# all input value is a string

# take 2 input and swap them
a = input("Enter first number: ")
b = input("Enter second number: ")

print("Before Swap:\n a: " + a + "\n b: " + b)

c = a
a = b
b = c

print("After Swap:\n a: " + a + "\n b: " + b)

## primitive data types in Python: int, float, boolean, string

# string : everything inside single or double quotes is string
# indexing start from 0 for all types of datastructures
print("Hello" [1]) # print the contents of index 1 # output: e
print("123" + "456") #output: 123456

#Integer
print(123 + 456) #output: 579
print(123_456_789) #output: 123456789 # `_` underscore is useful to format large number so that it can be read easily

#float
print(3.14159) # output: 3.14159
print(3.14_159) # output: 3.14159

#boolean : True, False || Notice first letter is capital
print(True)
print(False)


