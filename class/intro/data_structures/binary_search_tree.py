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

    def __iter__(self):
        def inorder_generator(root: Node) -> int:
            if root.left is not None:
                yield from inorder_generator(root.left)
            yield root.data
            if root.right is not None:
                yield from inorder_generator(root.right)
        return inorder_generator(self._root)

    def __reversed__(self):
        def revorder_generator(root: Node) -> int:
            if root.right is not None:
                yield from revorder_generator(root.right)
            yield root.data
            if root.left is not None:
                yield from revorder_generator(root.left)
        return revorder_generator(self._root)

    def __len__(self):
        return self._length


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    for v in bst:
        print(v)
    for v in reversed(bst):
        print(v)
