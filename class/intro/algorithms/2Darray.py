import sys
from typing import List, Tuple


def shortest_distance(matrix: List[List[int]]) -> List[Tuple[int]]:
    # min value
    min = sys.maxsize
    index1 = ()
    index2 = ()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if we are not on the last row
            if(i < len(matrix)-1):
                # check diff of next row
                diff = abs(matrix[i][j]-matrix[i+1][j])
                if diff < min:
                    min = diff
                    index1 = (i, j)
                    index2 = (i+1, j)
            # if we are not on the last column
            if(j < len(matrix[i])-1):
                # check diff of next column
                diff = abs(matrix[i][j]-matrix[i][j+1])
                if diff < min:
                    min = diff
                    index1 = (i, j)
                    index2 = (i, j+1)
    return [index1, index2]


def print_result(index1: Tuple[int], index2: Tuple[int], matrix: List[List[int]]) -> None:
    print(f"{index1}: {matrix[index1[0]][index1[1]]}")
    print(f"{index2}: {matrix[index2[0]][index2[1]]}")
    print(
        f"Difference: {abs(matrix[index1[0]][index1[1]]-matrix[index2[0]][index2[1]])}"
    )


def main():
    data = [[-22, 12, -33], [33, 62, 21], [54, 22, 42]]
    result = shortest_distance(data)
    print_result(result[0], result[1], data)


if __name__ == "__main__":
    main()
