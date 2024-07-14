# Python uses "Mersenne Twister" algorithm to generate random value

# first, we need to import random module

import random

random_integer = random.randint(1, 10)
# random.randint(l, r) returns a random integer between [l, r]
print(random_integer)

random_float = random.random()
# random.random() returns a random float between 0 and 1
print(random_float)

# example - 1: generate a random float between 0 and 5
# random() gives float between 0.0000 to 0.99999...
# if we multiply this value with 5, we get floating number between 0.0000 to 4.9999...
num = random.random() * 5
print(num)


### we can shuffle list, tuple, string
# to shuffle a list in place we can use: random.shuffle()
# to create a new shuffled list, string, tuple : new_list = random.sample(list, length of the list)
# random.shuffle() will throw error if we use it with tuple and string, since tuple and strings are immutable
# for more: https://note.nkmk.me/en/python-random-shuffle/
print("LIST")

list = [3, 1, 0, 2]
print(list)

random.shuffle(list)
print(list)

new_list = random.sample(list, len(list))
print(new_list)

print("TUPLE")

tup = (1, 3, 2, 4)
print(tup)

new_tup = random.sample(tup, len(tup))
print(new_tup)

print("STRING")
s = "abcde";

new_s = random.sample(s, len(s))
print(s)
print(new_s)

