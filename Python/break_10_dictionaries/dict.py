# it is same as map in c++
# syntax: {key : value}
# they are unordered, mutable(changeable) & don't allow duplicate keys
# we can use any data structure as value,i.e, list, dictionaries, tuples,set etc.
# But we can only use string, int, float, boolean, **tuples** as key
# why tuples can be used? Because tuples are immutable

my_dict = {"foyez": 10, "ahmed" : 20, "dewan" : 30}

print (my_dict["dewan"]) # output: 30

# print (my_dict["dawan"]) # KeyError: 'dawan' # this occurs if the key is not present on the dictionary

# we can use different type of key together
my_dict_2 = {"foyez": 10, 20 : "ahmed", "dewan" : 30}
print (my_dict_2[20])  #output: ahmed
print (my_dict_2["dewan"]) #output: 30

# adding a new key value pair
my_dict_2 ["yoo"] = 99  # {"yoo": 99}
# to print the dictionary
print (my_dict_2)    # output: {'foyez': 10, 20: 'ahmed', 'dewan': 30, 'yoo': 99}
# deleting a key value pair
my_dict_2.pop("yoo")
print (my_dict_2) #output: {'foyez': 10, 20: 'ahmed', 'dewan': 30}

# to clear an existing dictionary
my_dict_2 = {}
print (my_dict_2) # output: {}

# to clear an existing dictionary you can also use .clear() method
my_dict_2.clear()

# create an empty dictionary
empty_dict = {}  #this will create a new dictionary that is empty

# edit an item in a dictionary
print(my_dict)   #output: {'foyez': 10, 'ahmed': 20, 'dewan': 30}
my_dict["foyez"] = 100
print(my_dict)  #output: {'foyez': 100, 'ahmed': 20, 'dewan': 30}


## Nested Dictionary
student = {
  "name" : "Foyez",
  "subjects" : {
    "chem" : 80.0,
    "math" : 100,
    "phy" : "one hundread",
    "bio" : False
  }
}


# to print all the primary keys
print(student.keys()) # output: dict_keys(['name', 'subjects'])
# convert the key into a list
print(list(student.keys())) # output: ['name', 'subjects']
# size of a dictionary
print(len(student)) # output: 2
# to print all the values we can use .values() method
print(student.values())
#output: dict_values(['Foyez', {'chem': 80.0, 'math': 100, 'phy': 'one hundread', 'bio': False}])

# .items() method returns all (key, value) pairs as tuples
print(list(student.items())) # output: [('name', 'Foyez'), ('subjects', {'chem': 80.0, 'math': 100, 'phy': 'one hundread', 'bio': False})]

# we can access the value of a specific key in two methods
print(student["name"])   #output: Foyez
print(student.get("name")) #output: Foyez

# what is the difference between these two?
# print (studnet["Name"]) #KeyError: 'Name'
print(student.get("Name")) #output: None
# ## so the difference is , if we try to access a key that doesn't exist, we will get a KeyError in the first method, that will stops the program
# but in second case, if we try to access a key that doesn't exist, it will return None, the program will continue to run



##############################
new_dict = {"Country" : "Bangladesh"}
student.update(new_dict)
print (student)

# now see the difference
new_dict2 = {"Country" : "Dhaka"}
student.update(new_dict2)
print(student)
# value of "Country" key has been changed to Dhaka from Bangladesh because we can't have two different value with the same key

### Nesting a list in dictionary ###
my_dict = {
  "Country" : ["Bangladesh", "India", "Pakistan"],
  "Capital" : ["Dhaka", "New Delhi", "Islamabad"]
}

print (my_dict["Country"]) #output: ['Bangladesh', 'India', 'Pakistan']
print (my_dict["Capital"][1]) #output: 'New Delhi'

### Nesting a dictionary in a list
my_dict.clear() #to clear the dictionary

my_dict = [
  {"Country" : "Bangladesh", "Capital" : "Dhaka"},
  {"Capital" : "New Delhi", "Country" : "India"}
]

print(my_dict[0]) #output: {'Country': 'Bangladesh', 'Capital': 'Dhaka'}

# #looping through a dictionary

# # #one method
# for key in my_dict:
#   print(key)
#   print(my_dict[key])
#
# # #output:
# # # foyez
# # # 100
# # # ahmed
# # # 20
# # # dewan
# # # 30
#
# # #another method
# for key, value in my_dict.items():
#   print(key, value)

# #output:
# #foyez 100
# #ahmed 20
# #dewan 30
