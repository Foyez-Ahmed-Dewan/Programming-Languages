# traversing a list using for loop
my_list = [1, 2, 3, 4]

for x in my_list:
    print(x)

# intended lines are on the same block
for x in my_list:
    print(x)
    print(x)

# for loops and range function
# range(l, r) will run from l to r - 1
for i in range(1, 10):
    print(i)
# output: 1, 2, 3, 4, 5, 6, 7, 8, 9

# range(l, r, inc) will run from l to r - 1 by incrementing the value of current i with inc
for i in range(1, 10, 3):
    print(i)
#output: 1, 4, 7