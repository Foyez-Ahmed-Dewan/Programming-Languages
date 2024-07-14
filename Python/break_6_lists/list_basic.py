# declaration of a list
list = ['a', "b", 'c']  # notice, single quotes and double quotes doesn't matter

print(list)        #print the list , output: [a, b, c]
print(list [0])    #print the first element of the list, output : a
#positive index: 0, 1, 2,... , n - 1
#we can use negative index also, negative index indicates from last,i.e, [-n ,..., -3,-2, -1]
print(list[-1])  #output : c

list [1] = 'd' #change the value of the index 1 of the list
print(list)  #output: a, d, c

#to add a new element in the end of the list we can use append()
list.append("e")
print(list)  #output: a, d, c, e

#we can insert a new element in the list at a specific index using insert(index, item)
list.insert(1, "b")
print(list)  #output: a, b, d, c, e

#to remove an element from the list we can use remove(item), this will remove the 1st occurance of the item. If it doesn't exist, it will generate an valueError
list.remove("d")
print(list) #output: a, b, c, e

#pop() function remove the last element of the list
list.pop()
print(list) #output: a, b, c

# we can expand the list using extend keyword, in this way, we can insert a whole list into another list
list.extend(['u', 'a'])
print(list) #output: a, b, c, u, a
#we can delete value from specific index using del keyword
del list[3]
print(list) #output: a, b, c, a

#to count occurance of an item, use count(item)
print(list.count('a'))  #output: 2

#to reverse a list
print(list)  #output: a, b, c, a
list.reverse()
print(list)  #output: a, c, b, a

#to sort a list
list.sort(reverse = True) #sort in descending order
print(list) #output: c, b, a, a
list.sort() # sort in ascending order
print(list) #output: a, a, b, c

#print the first index of an item that exist in the list
print(list.index('a')) #output: 0
#print the index of an item starting at index 1
print(list.index('a', 1)) #output: 1

#length of a list: len() function is used
print(len(list)) #output: 4

#we can also add a list to the end of the list using extend()
arr = ["a", "b", "c"]
list.extend(arr)
print(list)  #output: a, a, b, c, a, b, c

# print(list[100]) #IndexError is same as run time error. If we try to access an index that is not present in the list, we get an IndexError

#to clear a list
list.clear()
print(list) #output: [] --> means list is empty now