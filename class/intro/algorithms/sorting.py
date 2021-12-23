from typing import List
from searching import create_random_list


def bubble_sort(array: List[int]) -> None:
    # creat flag to indicate if value has been swapped
    swapped = True
    end = len(array)-1
    # Keep repeating while swapped is True
    while swapped:
        # we haven't swapped anything this loop so swapped is false
        swapped = False
        for i in range(end):
            j = i+1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swapped = True
        end -= 1
    return array


def selection_sort(array: List[int]) -> None:
    for i in range(len(array)-1):
        # assume i is the smallest value
        m = i
        # look through all other elments
        for j in range(i, len(array)):
            # if value at j is smaller than value at m set m to j
            if array[j] < array[m]:
                m = j
        # if m is not i, we found a smaller value
        if m != i:
            array[m], array[i] = array[i], array[m]
    return array


def insertion_sort(array: List[int]) -> None:
    pass


def merge_sort(array: List[int]) -> None:
    pass


def main() -> None:
    data = create_random_list()
    print(bubble_sort(data))
    print(selection_sort(data))


if __name__ == "__main__":
    main()
