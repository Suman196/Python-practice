a = 20
b = 30
if a>b:
    print(f"a is larger than b {a} > {b} ")
else:
    print(f"a is smaller than b {a} < {b}")


print(bool(1))
print(bool(0))
print(bool(None))
print(bool(()))
print(bool(123))
print(bool("Suman"))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))