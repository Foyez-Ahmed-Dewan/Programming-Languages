# basic syntax: def is a keyword that is used to define a function
# def function_name():
#indented code blocks / functions body

# to call a function: function_name()

# ex - 1: create a function to print a message
def print_msg():
    print("Hello World")
    print("Hello")
    print("World")

print_msg()

# ## function with multiple parameters
def greet(name, age):  #notice, we no need to use data type name like c or c++
  print(f"Hello {name}, you are {age} years old.")

#positional argument -> argument passed in the order of the parameter
greet("Foyez", 20) #positional argument #here, name = "Foyez" and age = 20

greet(20, "Foyez") # here, name = 20, age = "Foyez"

#keyword argument -> parameters names are used to pass the argument
greet(age = 20, name = "Foyez") #here, name = "Foyez" and age = 20