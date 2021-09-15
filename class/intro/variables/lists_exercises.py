# lists_exercises.py

# 1. Sum all of the elements in the list
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum = sum(mylist)
# print(sum)

# 2. Write a program that removes all duplicates from a list
mylist = [1, 1, 1, 2, 3, 3, 3, 4, 5, 6]
print(list(set(mylist)))

# 3. Write a program that finds the interesection of two lists
# mylist1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
# mylist2 = [2, 2, 2, 3, 4, 4, 5, 5, 6]
# newlist = []
# for i in mylist1:
#     if i in mylist2:
#         newlist.append(i)
# for i in mylist2:
#     if i in mylist1:
#         newlist.append(i)
# print(sorted(newlist))

# 4. Write a program the finds the union of two lists, omitting duplicates
mylist1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
mylist2 = [2, 2, 2, 3, 4, 4, 5, 5, 6]
print(list(set(sorted(mylist1 + mylist2))))

# 5. Write a program that finds the differences of two lists
# mylist1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
# mylist2 = [2, 2, 2, 3, 4, 4, 5, 5, 6]
# newlist = []
# for i in mylist1:
#     if i not in mylist2:
#         newlist.append(i)
# for i in mylist2:
#     if i not in mylist1:
#         newlist.append(i)
# print(newlist)

# 6. Write a program that creates a list containing the frequencies of elements in a list
mylist = [1, 1, 1, 2, 3, 3, 3, 4, 5]
freq = 0
for i in mylist:
    if i in mylist:
        freq = freq + 1
    else:
        freq = 0
    print(freq)
