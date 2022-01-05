# data_structures/binary_search_tree.py
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.right: Node = None
        self.left: Node = None


class BinarySearchTree:
    def __init__(self):
        self._root: Node = None
        self._length: int = 0

    def insert(self, data: int) -> None:
        self._root = self._insert(data, self._root)

    def _insert(self, data: int, root: Node) -> Node:
        if root is None:
            self._length += 1
            return Node(data)

        if data < root.data:
            root.left = self._insert(data, root.left)
        else:
            root.right = self._insert(data, root.right)
        return root

    def __len__(self):
        return self._length


if __name__ == "__main__":
    pass
