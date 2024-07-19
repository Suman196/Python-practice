a = ["Suman","hi","jelo"]
print(len(a))
print(a[0])
list =[1,2,34,5]
list1 = [True, False]
print(len(list1))
print(len(list))
print(list[1])
print(list1[1])
#a list can contain diff typesof data
l = ["Suman",89, True,"salary"]
print(len(l))
print(l[2])
print(type(l))
l[1]=25
print(l)
t = ("apple","orange")
print(t)
t[0]="canned"
print(t)# will give errror as tuple is unchangeable



a = ["Apple ","Orange","Cherry", "kiwi", "melon", "mango"]

print(a[0])
print(a[-1])#the last one
print(a[1:5])# from  1 to 4 index
print(a[1:6])#from 1 to 5 index like 1 to m-1 a[1:m]
print(a[:4])#from 0(begining) to 3 
print(a[2:])#from 2 to last index 5
print(a[-5:-1])# from orange to melon not taking the last one

if "Apple " in a: # here only for single space this condition can be false and in "if" the condition is true then it will excute
    print("Yes present")
else:
    print("not present")




a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a[1]="Lebu"
print(a)
print(len(a))
a[2:5]=["Hagu","Padu","lol"]
print(a)
print(len(a))
a[1:3]=["lol1","lol2","lol3","lol4"]
print(a)#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
print(len(a))

a[2:7]=["Orange"]#so the orange takes from 2 to 6 index values or 2 to 6 space takes by orange
print(a)
print(len(a))

a.insert(1,"Cherry")# insert(index, value)
print(a)
print(len(a))