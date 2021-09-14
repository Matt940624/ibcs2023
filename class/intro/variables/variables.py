# Python is dynamically typed

# integer

myvar = 7
print(myvar)

# float

myvar = 7.3
print(myvar)

# string
myvar = "now i'm a string"
print(myvar)

myvar = "now i\'m a string"
print(myvar)

myvar = """
dkla;fjdklsafjdkls;afjkdls;afjkdls;a
ajkdlsajkdl;fja
sjkdflsajdklf;sd
ajdklfajdkl;f
"""
print(myvar)
a, b = 5, 10
print(f"a: {a}\t b:{b}")
a, b = b, a
print(f"a: {a}\t b:{b}")

myvar = 20
mytype = type(myvar)
print(mytype)

# Some operators are overloaded
a, b = 4, 6
result = a+b
print(result)

a, b = 4, 6.8
result = a+b
print(result)
