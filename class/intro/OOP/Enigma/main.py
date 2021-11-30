# main.py
import numpy.random as random


if __name__ == '__main__':
    random.seed(100)
    for i in range(5):
        print(random.randint(1, 100))
