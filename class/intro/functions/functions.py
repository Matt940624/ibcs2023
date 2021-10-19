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
