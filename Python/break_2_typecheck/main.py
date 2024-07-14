num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters")
# this will generate a TypeError. Here num_char is integer, concatenation between strings and integer is not possible

#we can use typecast to convert num_char into string
print("Your name has " + str(num_char) + " characters")

#type checking: type (x) is used to get the type of an object `x`
print(type(num_char))    #output: <class 'int'>
print(type("Hello"))    #output: <class 'str'>
print(type("123.45"))   #output: <class 'str'>
print(type(123.45))     #output: <class 'float'>


#in python, input function always returns a string
a = input()
print(type(a)) #output: <class 'str'>

c = input()
d = input()

print(c + d) #output: (c + d) as string

#type conversion
a = 3
b = 5

c = a + b
print(c) #output : 8

c = str(a) + str(b)
print(c) #output : 35

a = 3.67
print(int(a)) #output : 3
print(str(a)) #output : 3.67

a = 50
print(float(a)) #output : 50.0

b = 50.6

print(int(a) + int(b)) #output : 100
print(int(a) + float(b)) #output: 100.6
# print(int(a) + str(b))  #error

a = int(input())
print(type(a)) #output: <class 'int'>