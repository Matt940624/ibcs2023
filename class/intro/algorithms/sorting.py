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
    # starting at the 2nd element of the array
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        # while we find values greater than key
        # swap j and j+1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


def merge_sort(array: List[int], left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(array)-1
    if right <= left:
        return

    mid = (right+left)//2
    merge_sort(array, left, mid)
    merge_sort(array, mid+1, right)
    merge(array, left, mid, right)


def merge(array: List[int], left: int, mid: int, right: int):
    i = left
    j = mid+1
    k = 0
    tmp = [0]*(right-left+1)
    while i <= mid and j <= right:
        if array[i] < array[j]:
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1
        k += 1

    while i <= mid:
        tmp[k] = array[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = array[j]
        j += 1
        k += 1
    # copy temporary array back into orginal array
    k = 0
    while left + k <= right:
        array[left+k] = tmp[k]
        k += 1


def main() -> None:
    data = create_random_list()
    print(data)
    # print(bubble_sort(data))
    # print(selection_sort(data))
    # print(insertion_sort(data))
    merge_sort(data)
    print(data)


if __name__ == "__main__":
    main()
