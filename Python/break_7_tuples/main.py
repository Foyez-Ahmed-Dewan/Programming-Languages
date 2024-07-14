# tuples are immutable, we can't change the value of a tuple once it is initialized
tup = () # this is an empty tuple
print(tup) #output: ()

#notice the difference between this two cases
tup2 = (1)
print(type(tup2)) #outuput: <class 'int'>
print(tup2) #output: 1

tup3 = (1, )
print(type(tup3)) #output: <class 'tuple'>
print(tup3) #output: (1)
#when there is only 1 element in a tuple, we need to add a comma after the element to indicates that it is a tuple otherwise compiler assumes it as an integer

my_tup = (1, 2, 3, 4, 5, 1) # notice, 1st bracket is used
print(my_tup) #output: (1, 2, 3, 4, 5, 1)

# my_tup[1] = 10 #we can't change the value of a tuple

#slicing a tuple is as same as list
print(my_tup[1 : 4]) #output: (2, 3, 4)

#count occurences of an item
print(my_tup.count(1)) #output: 2
#returns index of 1st occurences of an item
print(my_tup.index(1)) #output: 0


















