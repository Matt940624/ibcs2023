# 1
# Write a python program to count and return a dictionary of character
# frequencies in a given string

# Sample String: 'google.com'
# Expected Result: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

import locale
text = "google.com"
freq = {}


def counter(string, dictionary):
    for i in string:
        if i in freq:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    output = f"Answer 1 for #1: {freq}"
    return output


print(counter(text, freq))


# 2
# Write a Python function to insert a string in the middle of a string
# Sample function and result:
# insert_string_middle('[[]]', 'Python') -> [[Python]]
# insert_string_middle('{{}}', 'PHP') -> {{PHP}}
# insert_string_middle('|||', 'Unbalanced') -> |Unbalanced||

wrapper = "(())"
interior = "Python"


def insert(symbol, text):
    length = len(symbol)
    # divide = int(length / 2)
    divide = length // 2
    output = symbol[:divide] + text + symbol[divide:]
    return output


print(insert(wrapper, interior))


# 3
# Write a Python program to display a number with a comma separator.
# Sample function and result:
# comma_sep("1102") => 1,102
# comma_sep("2340340958") => 2,340,340,958
# Advanced: comma_sep("2340340958", 4) => 23,4034,0958

number = 1102454124983548
comma_sep = "3"


def comma(number):
    locale.setlocale(locale.LC_ALL, "zh_TW")
    output = "{:n}".format(number)
    return output


print(comma(number))

# 4
# Write a Python program to move spaces to the front of a given string.
# Sample function and result:
# front_pack("This is a sentence with several spaces") =>
#       "      Thisisasentencewithseveralspaces"
text = "This is a sentence with several spaces"


def space_remove(text):
    output = text.replace(" ", "")
    return output


print(space_remove(text))

# 5
# Write a Pythong program to compute sum of digits of a given number string
number = "123"


def sum(number):
    output = 0
    for i in number:
        output = output + int(i)
    return output


print(sum(number))

# 6 Write a Python program to determine if a set of parenthesis are balanced
# (()((()(())())())))()))))(())())()
text = "()(())("


def check_balance(text):
    brackets = ["()", "[]", "{}"]
    while any(x in text for x in brackets):
        for br in brackets:
            text = text.replace(br, "")
    if not text:
        output = "balanced"
        return output
    else:
        output = "unbalanced"
        return output


print(check_balance(text))
