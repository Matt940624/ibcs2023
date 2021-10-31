# Write a function that calculates a factorial
# factorial(5) -> 120
# factorial(7) -> 5040
# factorial(10) -> 3628800


def factorial(n: int) -> int:
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x


print(factorial(4))


# Write a function that calculates a permutation
# n! / (n-r)!
# nPr(10, 10) -> 3628800
# nPr(10, 7) -> 604800
# nPr(10, 4) -> 5040
def nPr(n: int, r: int) -> int:
    x = 1
    for i in range(1, n+1):
        x = x * i
    y = 1
    for i in range(1, (n-r)+1):
        y = y * i
    result = int(x/y)
    return result


print(nPr(10, 7))


# Write a function that calculates a combination
# n! / (r!(n-r)!)
# nCr(10, 10) -> 1
# nCr(10, 7) -> 120
# nCr(10, 4) -> 210
def nCr(n: int, r: int) -> int:
    # n!
    x = 1
    for i in range(1, n+1):
        x = x * i
    # (n-r)!
    y = 1
    for i in range(1, (n-r)+1):
        y = y * i
    # r!
    z = 1
    for i in range(1, r+1):
        z = z * i
    result = int(x/(y*z))
    return result


print(nCr(10, 7))

# Write a function that returns a list of n rows of Pascal's Triangle
# pascals_triangle(3) -> [[1], [1, 1], [1, 2, 1]]
# pascals_triangle(6) -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
# pascals_triangle(9) -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]]


def pascals_triangle(n: int) -> list:
    pass


# Write a generator that produces a string of * characters, each line one * longer than the previous
# gen = star_gen()
# next(gen) -> *
# next(gen) -> **
# next(gen) -> ***
# next(gen) -> ****
# next(gen) -> *****


def star(n) -> str:
    for i in range(0, n):

        for j in range(0, i + 1):

            print("* ", end="")

        print()


print(star(3))


# Seive of eratosthenes
# Create a generator function that will return the next prime number using
# the seive of eratosthenes
# gen = prime()
# next(gen) -> 2
# next(gen) -> 3
# next(gen) -> 5
# next(gen) -> 7
# next(gen) -> 11
def next_prime(n) -> int:
    numbers = range(2, n)
    while len(numbers) > 0:
        yield numbers[0]
        numbers = [num for num in numbers if num %
                   numbers[0] != 0 or num == numbers[0]]


gen = next_prime(10)
print(next(gen))


print(next_prime(10))

# Write a generator function that returns the next row of
# Pascal's Triangle each time it is called
# gen = pascals_triangle_gen()
# next(gen) -> [1]
# next(gen) -> [1, 1]
# next(gen) -> [1, 2, 1]
# next(gen) -> [1, 3, 3, 1]
# next(gen) -> [1, 4, 6, 4, 1]


def pascals_triangle_gen() -> list:
    pass
