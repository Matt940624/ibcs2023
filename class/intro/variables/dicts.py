mydict = {
    "give_name": "matymio",
    "family_name": "miomio",
    "age": 17
}

print(mydict)

# dictionairies do NOT stor keys in any pariticular order
dictItems = mydict.items()
print(dictItems)

# Iterating over a dict
for k, v in mydict.items():
    print(f'Key: {k}\tVlaue: {v}')

for k in mydict.keys():
    print(f"Key:{k}")

for v in mydict.keys():
    print(f"Key:{v}")

hasKey = 'given_name' in mydict
print(hasKey)
hasKey = "DNE" in mydict
print(hasKey)


# Accessing data in a dictionary
givenName = mydict["give_name"]
print(givenName)
# Not SAFE
# middleName = mydict["middle_name"]
# print(middleName)

# Safer method
givenName = mydict.get("give_name")
print(givenName)
middleName = mydict.get("middle_name")
print(middleName)

familyName = mydict.pop("family_name")
print(familyName)
print(mydict)

something = mydict.popitem()
print(something)
print(mydict)

mydict.clear()
print(mydict)

mydict["one"] = 1
mydict["two"] = 2
print(mydict)
