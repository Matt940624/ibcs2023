import sys
from typing import Text

text = "this is a string"
text = "this is a strong"
text = """this is a strong that preserves the whitespace 
I can make it more than one line
and the new lines will be preserved"""

print(text)

text = "I\'m a string. \n This is a new line \n \t I'm indented"
print(text)

text = r"Special characters do nothing \n\n See, no new lines"
print(text)

print(sys.getdefaultencoding())

# Unicode characters
text = "The circumference of a circle is 2 \u03c0r"
print(text)

text = "\u6211\u6703\u5beb\u4e2d\u6587"
print(text)

text = "I'm a long sentence with a lot of uselesss words"
# Strings are immutable
sub = text[10:]
print(sub)
sub = text[:10]
print(sub)
sub = text[10:20]
print(sub)


text = "42"
number = text.isdigit()
letter = text.isalpha()
starts_with_cap = text.istitle()
print(number, letter, starts_with_cap)

text = "    \n\n\t\t\r\r"
space = text.isspace()
print(space)
length = len(text)
print(length)
countL = text.count('l')
print(countL)

text = "I'm a long sentence with a lot of uselesss words"
print(text.title())
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.swapcase())

text = "I'm a bit shorter"
newText = text.center(30)
print(newText)
newText = text.rjust(30)
print(newText)
text = "The big blue bird is biting the branch"
newText = text.replace("b", "x")
print(newText)
newText = text.replace("b", "x", 1)
print(newText)
words = text.split(" ")
print(words)
words = text.split("b")
print(words)
start = text.startswith('T')
print(start)
start = text.startswith('T', 5, 10)
print(start)
end = text.endswith('T')
print(end)
loc = text.find('bi')
print(loc)
loc = text.find('bi', loc+1)
print(loc)
loc = text.rfind('bi')
print(loc)
loc = text.find("z")
print(loc)

loc = text.find('bi')
print(loc)
loc = text.index('bi')
print(loc)
loc = text.find('z')
print(loc)
# loc = text.index('z')
# print(loc)

words = ["One", "Two", "Three", "Four"]
text = " ". join(words)
print(text)
text = "\t".join(words)
print(text)
text = "\n".join(words)
print(text)
text = "student,".join(words)
print(text)
