#basic operators : +, -, *, /

print(5 + 2) # 7
print(5 - 2) # 3
# division (/): always returns float value even if result is an integer
print (10 / 2) #5.0
print(11 / 2) # 5.5 [notice the difference with C++]

#multiplication
print (5 * 2) # 10
#exponentiation : x ** y = (x^y)
print (5 ** 2) # 25

#order of operations : PEMDAS
#parenthesis
#exponentiation
#multiplication, division : associativity L to R
#addition, subtraction : associativity L to R

#rounding off: convert the result into nearest integer
print(8 / 3) #output: 2.66...5
print(round(8/ 3)) #output: 3
print(round(8 / 3, 2)) #output: 2.67
#round (x / y, p) returns x/y rounded to p decimal places

#floor division: returns an integer x that is less than or equal to actual value
print(8 // 2) #output: 4
print(8 // 3) #output: 2

#increment (++) and decrement (--) operators are not allowed in python
#instead we can use +=, -=, *=, /= operators

#logical operators: and (&) , or(|) , not (~), xor (^), left shift (<<), right shift (>>)

# 6 = 110, 3 = 011
print (6 & 3) # 2
print (6 | 3) # 7
print(~3)     # -4
print(6 ^ 3)  # 5
print (6 << 2) # 24
print (6 >> 1) # 3



######### F - string##########
scr = 200

# print ("Your score is " + scr) # this is invalid
print ("Your score is " + str (scr)) # this is valid, but here scr is converted into string
#if we don't want to convert the datatypes, and we need to print string with another datatype together, we can use f-string
print (f"Your score is {scr}")

height = 1.8
isWinning = True

print (f"Your score is {scr}, your height is {height}, your wining situation is: {isWinning}")

