# functions.py


def myFunc():
    print("I'm a function")


myFunc()


def area(w: float, h: float) -> float:
    """area function returns the area of the quadrilateral
    Attributes
        w: width of the quadrilateral
        h: height of the quadrilateral
    Returns:
        width * height
    """
    return w * h


a = area(4, 5)
print(a)


def increment(x: int) -> None:
    x = x + 1


x = 5
print(x)
increment(x)
print(x)


def incrementList(x: list) -> None:
    x[0] = x[0] + 1


x = [5]
print(x)
incrementList(x)
print(x)


def nth_root(num: float, root: int, prec: float = 1e-15) -> float:
    if(num < 0 and root % 2 == 0):
        raise ValueError(f"No even roots of negative numbers: num = {num}")
    if(root < 0):
        raise ValueError(f"No negative roots: root ={root}")
    if(num == 0):
        return 0
    if(root == 0):
        return 1

    def f(x: float, r: float, g: float) -> float:
        return g ** r-x

    def df(r: float, g: float) -> float:
        return r * g ** (r-1)
    # This is our intitial guess at an answer
    # there are more advanced ways to choose this
    guess = 1
    prev = 0
    while abs(guess-prev) > prec:
        prev = guess
        guess -= f(num, root, guess)/df(root, guess)
    return guess


r = nth_root(2, 2)
print(r)


r = nth_root(root=4, num=81)
print(r)

# In Python, functions are first-class members
myvar = nth_root

r = myvar(num=625, root=4)
print(r)


def even_handler(val: int) -> None:
    print(f"{val} is divisalbe by 2")


def odd_handler(val: int) -> None:
    print(f"{val} is not divisable by 2")


def do_a_thing(even_callback, odd_callback) -> None:
    for i in range(20):
        if i % 2 == 0:
            even_callback(i)
        else:
            odd_callback(i)


do_a_thing(even_handler, odd_handler)

# Generators


def squares() -> int:
    n = 1
    while True:
        yield n**2
        n += 1


val = squares()
for i in range(100):
    print(next(val))


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


gen = fibonacci_numbers(20)
for _ in range(20):
    print(next(gen))
