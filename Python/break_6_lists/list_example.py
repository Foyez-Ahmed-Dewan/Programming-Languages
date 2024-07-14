## check if a list is a palindromic list or not
# first method: this method is not working properly
list1 = [1, 2, 3]
list2 = list1   # here , it performs deep copy of list1

list2.reverse() # when we are reversing list2, it also reverses list1 due to deep copy earlier

print (list1) # output: [3, 2, 1] but actual list1 = [1, 2, 3]
print (list2)
#second method
list3 = [1, 2, 3]

list4 = list3.copy() #it performs shallow copy, so any operation we apply in list4, doesn't reflect in list3

list4.reverse()
print(list3)
print(list4)

# now , lets use second method to check if a list is palindromic or not
list5 = [1, 2, 3, 4, 5, 4, 3, 2, 1]

list6 = list5.copy()

list6.reverse()

if list5 == list6:
    print("Palindromic list")
else:
    print("Non-palindromic list")