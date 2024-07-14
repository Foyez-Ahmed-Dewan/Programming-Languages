my_list = [1, 2, "a", 3, 'b'] # list can contain different data types together
print(my_list)  #output: 1, 2, 'a', 3, 'b'

# pop(idx) is used to remove item of a list at a specific index
my_list.pop(2)
print(my_list)  #output: 1, 2, 3, 'b'

# string is immutable means we can't change specific index of a string
# list is mutable means we can change specific index of a list

my_string = "Hello"
# # my_string[0] = "H" #TypeError: 'str' object does not support item assignment
my_list [1] = "Hello"
print(my_list) #output: 1, 'Hello', 3, 'b'

# list slicing : we can use list slicing to get a subpart of a list
# list_name [starting_idx : ending_idx] #  ending_idx is not included

marks = [100, 80, 90, 30, 10, 50]

print(marks[1 : 4]) #output: 80, 90, 30
print(marks[2 : ])  #starting_idx = 2, ending_idx = len(list) #output: 90, 30, 10, 50
print(marks[ : 4]) #starting_idx = 0, ending_idx = 4 #output: 100, 80, 90, 30
print(marks[-3 : -1]) #output: 30, 10
print(marks[-2 : -3]) #starting index <= ending index , otherwise it will give [] this as output
print(marks[1 : 1]) # empty

# total sum of value of a list
ttl_sum = sum(marks, 0)  #sum(list_name, initial_sum)
print(ttl_sum)


#### there is no built in function to reverse the string
str = "hello world"

# str.reverse()  # no function
# to reverse a string, we can slice the string in opposite order
str = str[::-1]

print(str) #output: dlrow olleh