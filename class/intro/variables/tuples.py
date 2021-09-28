# Tuples are like lists, but immutable (can't be changed later)
#  Because they can't be mutated, they are slightly more space efficient

import sys
import time

a_list = [1, 2, 3, 4, 5]
a_tuple = (1, 2, 3, 4, 5)
print('a_list size: ', sys.getsizeof(a_list))
print('a_tuple size: ', sys.getsizeof(a_tuple))

# average_time =0
# iterations =

# for i in range(iterations):
#     start_time = time.time()
#     b_list = list(range(1000000))
#     end_time = time.time()
#     average_time += (end_time - start_time)
# average_time/= 100

# print(f"Size    ")


mytuple = (5,) * 10
print(mytuple)
print(f"Address: {hex(id(mytuple))}")

mytuple = mytuple + (1, 2, 3)
print(mytuple)
print(f"Address: {hex(id(mytuple))}")
