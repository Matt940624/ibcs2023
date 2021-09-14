mylists = [5, 10, 15, 20]
print(mylists)
mytype = type(mylists)
print(mytype)

print(mylists[0])
print(mylists[1])
print(mylists[2])
print(mylists[3])

for val in mylists:
    print(val)

for val, idx in enumerate(mylists):
    print(f"{idx}: {val}")

i = 0
while i < len(mylists):
    print(mylists[i])
    i = i + 1

for i in range(len(mylists)):
    print(mylists[i])

# Append adds to the END of the list
mylists.append(25)
print(mylists)

length = len(mylists)

mylist = [1, 2.5, "3.5", [4.5, 5.5], (6, 7)]
print(mylist)
print(len(mylist))

mylist = [0]*15
print(mylist)
mylist = [1, 2, 3]*5
print(mylist)

lista = [1, 2, 3]
listb = [4, 5, 6]
listc = lista + listb
print(listc)

# Find out if an element is in an array
mylist = ['a', 'b', 'c', 'd', 'e', 'f']
print("c" in mylist)
print("c" not in mylist)
print("z" in mylist)
print("z" not in mylist)

# Searching for location in list
idx = mylist.index("c")
print(idx)

idx = mylist.index("e", 3, 5)
print(idx)

# Inserting into list
mylist.insert(3, "z")
print(mylist)

# Remove a specific element from the list
mylist.remove("z")
print(mylist)

popped = mylist.pop()
print(mylist, popped)

popped = mylist.pop(2)
print(mylist, popped)

# Count things in a list
cnt = mylist.count("a")
print(cnt)

mylist.extend(['z', 'e', 'w', "j"])

# Sorting a list
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

# List Comprehensions
mylist = []
for i in range(10):
    mylist.append(i)
print(mylist)

mylist = [x for x in range(10)]
print(mylist)

mylist = [x for x in range(10) if x % 2 == 0]
print(mylist)

mylist = [x for x in range(0, 10, 2)]
print(mylist)

mylist = [(x*3)for x in range(10)]
print(mylist)


filtered = [x for x in mylist if x % 2 == 0]
print(filtered)

maxVal = max(mylist)
filtered = [(maxVal-x)for x in mylist if x > 5 and x < 25]
print(filtered)


mylist = [x for x in range(20)]
# Slicing start:end:stop
sublist = mylist[3:5]
print(sublist)

sublist = mylist[3:15:2]
print(sublist)

sublist = mylist[15:3:-2]
print(sublist)

sublist = mylist[7:]
print(sublist)

sublist = mylist[7::3]
print(sublist)

sublist = mylist[:10]
print(sublist)
