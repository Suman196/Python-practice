# Loop list
a = ["apple", "banana", "cherry","kiwi", "orange"]
for c in a:
    print(c)
print("\n")
for i in range(len(a)): # traverse index from 0 to 4
    print(a[i])

print("\n")

i = 0;
while(i<len(a)):
    print(a[i])
    i=i+1

print("\n")# new line
[print(x) for x in a]#List Comprehension offers the shortest syntax for looping through lists

# list comprehension

x = ["apple", "banana", "cherry", "kiwi", "mango"]
new=[]
for i in x:
    if "a" in i:
        new.append(i)

print(new)

new = [i for  i in x if "a" in i ]
print(new)

new = [i for i in x if "a" not in i]
print(new)

new = [i for i in x if i!="apple"] 
print(new)

new = [i for i in x] # not condition
print(new)

# printing x array upto 10 times beacuse 0 to 9
new =[ x for i in range(10)] 
print(new)

new =[ y for y in range(10) ] # array with in it condition inserted
print(new)

new = [ y for y in range(10) if y<5]
print(new)
for i in range(10):
    print(i)# kisko print karna hai i.e i

#new =[kisko print karwana hai for item in iterable if condition== true]


x = ["apple", "banana", "cherry", "kiwi", "mango"]
new=[]

new =[i.upper() for i in x ]
print(new)

new =["Hello" for i in x] # all the array elements will be replaced by "Hello"
print(new)

new = [ i if i!="apple" else "orange" for i in x] # i if i did not got apple then goto else(i==apple) make apple ,orange
print(new)
#Return the item if it is not apple, if it is apple return orange

new = [ i if i=="apple" else "orange" for i in x] # i if i got apple it's true then goto else(i!=apple) make other elements are orange
print(new)

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
# To sort descending, use the keyword argument reverse = True