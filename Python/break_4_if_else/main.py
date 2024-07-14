# example - 1: take an input , if the input is greater than 100 print "greater than 100", else print "less than 100"

num = int(input())

if num > 100:
    print("Greater than 100")
else:
    print("Less than 100")


# everything that is intended after the if statement is considered as part of the if statement
if num > 100:
    print("Greater")
    print("than")
    print("100")
else:
    print("Less")
    print("than")
    print("100")

# what if the number is == 100? we ignored this case, now change the code
if num > 100:
    print("Greater than 100")
elif num == 100:
    print("Equal to 100")
else:
    print("Less than 100")


# example -2: take an input and check if the input is an even number or an odd number
number = int(input())

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


# ############## Nested else if ################
# example - 3: Write a program that will determine if a student can ride a car or not. If someone's height are above 100cm and his/her age is greater than or equal to 18, he/she can ride the car. Otherwise it is impossible for him to ride the car.
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

if height > 100:
    if age >= 18:
        print("can ride the car")
    else:
        print("can't ride the car")
else:
    print("can't ride the car")

# another way
if height > 100 and age >= 18:
    print("can ride the car")
else:
    print("can't ride the car")


##example -4: take a number, if it is greater than 100 print "greater than 100", if it is between 50 and 100 print "between 50 and 100", if it is less than 50 print "less than 50"
num2 = int(input())

if num2 > 100:
    print("Greater than 100")
elif num2 <= 100 and num2 >= 50:
    print("between 50 and 100")
else:
    print("less than 50")









