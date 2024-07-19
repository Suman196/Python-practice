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

