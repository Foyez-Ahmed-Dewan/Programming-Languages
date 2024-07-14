# '#' is used for commenting purpose
# 'print' is used to display the output
# we can use single or double quotes inside the print function, doesn't matter
print('Hello World')  #output: Hello World
print("Hello World")  #output: Hello World

#print modifiers : 3 ways
print("A 'single quote' inside a double quote")
print('A "double quote" inside a sinlge quote')
# if you use double quotes inside a double quotes, you need to use escape operator('\`) to escape the inneer double quote
print("Alternatively you can just \"escape\" the quote")

#print modifiers : example
print("She said : 'Hello' and then left.")      #output: She said : 'Hello' and then left.
print('She said : "Hello" and then left.')      #output: She said : "Hello" and then left.
print("She said : \"Hello\" and then left.")    #output: She said : "Hello" and then left.

print('e.g. print("Hello " + "World")')    #output: e.g. print("Hello " + "World")

# to go to new line, use `\n`
print("Hello\nFoyez")
#output:
#Hello
#Foyez

print ("Hello" + " " + "Foyez") #Hello Foyez
print ("Hello " + "Foyez")     #Hello Foyez

#***in Python, indentation is very important
    # print("hello world") #this code generates an error because of indentation, all code should start at the begining of the line

###input function
input("What is your name? ") #it will take the input from the user as a string on the same line
input("Enter a number ") #input function always takes input as ***string***

print(input("What is your name? ")) #it will take input from the user, then will print the given input value on a new-line

#to find the length of a string, we can use `len` function
print(len(input("What is your name? "))) #it will print the length of the input string

print(len("Foyez Ahmed")) #11

# print(len(12345)) # this will generate an error because `len` function cab be used with only STRINGs

### how to take integer input
a = int(input())
print(a)

### how to take multiple integer as input in the same line
a, b = map(int, input().split())
print(a, b)

## how to assign multiple variables in the same line
a, b, c = 0, 0, 0

print(a, b, c) #output: 0 0 0

a, b, c = 10, 1, 100
print(a, b, c) #output: 10 1 100