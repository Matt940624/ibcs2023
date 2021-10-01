# lists_exercises.py

# 1. Sum all of the elements in the list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(mylist))

# 2. Write a program that removes all duplicates from a list
mylist = [1, 1, 1, 2, 3, 3, 3, 4, 5, 6]
print(list(set(mylist)))

# other solutions
for val in mylist:
    while mylist.count(val) > 1:
        mylist.remove(val)

# other solution
newlist = [x for i, x in enumerate(mylist) if mylist.index(x) == i]

# other solution
newlist = [x for i, x in enumerate(mylist) if x not in mylist[i + 1:]]
# 3. Write a program that finds the interesection of two lists
mylist1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
mylist2 = [2, 2, 2, 3, 4, 4, 5, 5, 6]
newlist = []
for i in mylist1:
    if i in mylist2:
        newlist.append(i)
for i in mylist2:
    if i in mylist1:
        newlist.append(i)
print(sorted(list(set(newlist))))

# If we want not duplicates
newlist = [i for i in mylist1 if i in mylist2]
print(newlist)

# other solutions
newlist = [x for i, x in enumerate(
    mylist1)if x in mylist2 and mylist1.index(x) == i]

# 4. Write a program the finds the union of two lists, omitting duplicates
mylist1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
mylist2 = [2, 2, 2, 3, 4, 4, 5, 5, 6]
print(list(set(sorted(mylist1 + mylist2))))

# 5. Write a program that finds the differences of two lists
mylist1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
mylist2 = [2, 2, 2, 3, 4, 4, 5, 5, 6]
newlist = []
for i in mylist1:
    if i not in mylist2:
        newlist.append(i)
for i in mylist2:
    if i not in mylist1:
        newlist.append(i)
print(newlist)

newlist = [i for i in mylist1 if i not in mylist2]
newlist += [i for i in mylist2 if i not in mylist1]
print(newlist)

# 6. Write a program that creates a list containing the frequencies of elements in a list
mylist = [1, 1, 1, 2, 3, 3, 3, 4, 5]
freq = {}
for i in mylist:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

for val in mylist2:
    newlist += [(val, mylist1.count(val))]

freq = [(x, mylist1.count(x))
        for i, x in enumerate(mylist1) if i == mylist1.index(x)]

# dkla;jdklf;sajsdklfa