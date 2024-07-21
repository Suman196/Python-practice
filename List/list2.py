x =["orange", "mango", "kiwi", "pineapple", "banana"]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

a = [100, 50, 65, 82, 23]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50) # sort the number that should be nearer toi 5o means the substarction should be less (from the substraction 50)
a.sort(key=myfunc)
print(a)

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
x = ["banana", "Orange", "Kiwi", "cherry"]
x.sort()
print(x)

# Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function
x = ["banana", "Orange", "Kiwi", "cherry"]
x.sort(key = str.lower)
print(x)

# The reverse() method reverses the current sorting order of the elements
x.reverse()
print(x)

# Make a copy of a list with the copy() method
x = [ 100,20,5,0,5,6]
y = x.copy()
print(y)

# Another way to make a copy is to use the built-in method list()
z = list(x)
print(z)

#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
x = [ 100,20,5,0,5,6]
y = x.copy()
y = x+y
print(y)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2: # # we have to give for loop other wise it will attach sign of array with a
  list1.append(x)

print(list1) 

#Use the extend() method to add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
















