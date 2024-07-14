# ex - 1: find the area of a rectangle
def calculate_area (length, width):
    area = length * width
    return area

length = int(input("Enter length of the rectangle: "))
width = int (input("Enter width of the rectangle: "))

print(f"Area of the rectangle is : {calculate_area(length, width)}")


# example - 2: check a given number is prime or not
import math
def isPrime (num):
    for i in range (2, (int)(math.sqrt(num) + 1)):
        if (num % i == 0):
            return False

    return True


# code begins here
number = int(input("Enter a number: "))

if (isPrime(number)):
    print(f"{number} is a prime number")
else:
    print(f"{number} is a not prime number")



# example - 3 : take first name and last name as input. By using a function, return the full name
# .title() function is used to convert the string into title case -> first letter of each word is capitalized
def Give_Full_Name (first_name, last_name):
  if (first_name == "" or last_name == ""):
    return "You didn't provide valid inputs"

  full_name = first_name + " " + last_name
  full_name = full_name.title() # remember, it returns the title case of the string
  return full_name

first_name = input("Enter your first name: ")
last_name = input ("Enter your last name: ")

print (f"Your full name is: {Give_Full_Name(first_name, last_name)}")



## example - 4 : Take a year and a month number as input, print number of days as output. You should conside leap year as well.
def isLeapYear (year):
  if (year % 4 == 0):
    if (year % 100 == 0):
      if (year % 400 == 0):
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31]

  if (month == 2 and isLeapYear(year)):
    return 29
  else:
    return month_days[month - 1]

# main function
year = int(input("Enter a year: "))
month = int(input("Enter a month number: "))

print (f"Number of days in {month} of {year} is: {days_in_month(year, month)}")