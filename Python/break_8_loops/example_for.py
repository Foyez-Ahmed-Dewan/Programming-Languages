# ex - 1: find the sum of natural number from 1 to 100

ttl_sum = 0

for i in range (1, 101):
    ttl_sum += i

print(f"Sum of the natural numbers from 1 to 100 is: {ttl_sum}")

# ex - 2: find the sum of all the even numbers from 1 to a given number
r = int(input("Enter the value of upper bound: "))

even_sum = 0

for i in range (1, r + 1):
    if i % 2 == 0:
        even_sum += i
# this can be done by below approach also
# for i in range (2, r + 1, 2):
#   even_sum += i

print(f"Sum of all the even numbers between 1 to {r} is : {even_sum}")

# example - 3: Your program should print each number from 1 to 100 in turn. If the number is divisible by 3 , print "Fizz" instead of the number. If the number is divisible by 5 , print "Buzz" instead of the number. If the number is divisible by both 3 and 5 , print "FizzBuzz" instead of the number.

for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



# example - 4: given a list of student marks. Find average marks obtained by the students.

marks = input().split() #taking the whole list as input and then splitting it into a list

ttl_marks = 0
ttl_stu   = 0

for x in marks:
  ttl_marks += int(x) #we need to type cast since by defualt, input is string
  ttl_stu += 1

print(f"Average marks obtained by the students is: {ttl_marks / ttl_stu}")



###example - 5: given a list of students marks. Find the highest marks obtained by the students.
marks = input().split()

highest_marks = -1

for x in marks:
  mark = int(x)
  if (mark > highest_marks):
    highest_marks = mark

print(f"The highest marks obtained by the students is : {highest_marks}")






