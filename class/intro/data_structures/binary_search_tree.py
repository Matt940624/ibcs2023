# data_structures/binary_search_tree.py
from os import linesep
from typing import Callable


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.height: int = 0
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

        self._height(root)
        return root

    def delete(self, data: int) -> None:
        self._delete(data, self._root)

    def _delete(self, data: int, root: Node) -> Node:
        if self._root is None:
            return None
        # if data is less than current root data
        # traverse down left subtree
        if data < root.data:
            root.left = self._delete(data, root.left)
        # if data is greather than current root data
        # traverse down right subtree
        elif data > root.data:
            root.right = self._delete(data, root.right)
        else:
            self._length -= 1
            # if there is only a right subtree
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            # if ther is only a left subtree
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp
            # node has two children choose the smallest in-order successor
            tmp = self._min_node(root.right)
            root.data = tmp.data
            root.right = self._delete(tmp.data, root.right)
        return root

    def _min_node(self, root: Node) -> Node:
        if root.left is not None:
            return self._min_node(root.left)
        return root

    def height(self) -> int:
        return self._root.height

    def _height(self, root: Node) -> int:
        if root is None:
            return -1
        root.height = max(self._height(root.left),
                          self._height(root.right)) + 1
        return root.height

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


def tree_printer(root: Node, data_function: Callable, width: int = 64):
    elem_cnt = 2 ** (root.height + 1) - 1
    elms = [None] * elem_cnt

    def flatten(root: Node, idx: int = 0):
        elms[idx] = data_function(root)
        if root.left:
            flatten(root.left, idx*2+1)
        if root.right:
            flatten(root.right, idx*2+2)
    flatten(root)

    def value_str(val: int, width: int):
        if val is None:
            return "_".center(width)
        return f"{val}".center(width)
    level = 0
    end = 0
    level_width = width
    s = ""

    for i, val in enumerate(elms):
        s += value_str(val, level_width)
        if i == end:
            s += linesep
            level_width = level_width//2
            level += 1
            end += 2**level
    return s


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(3)
    bst.insert(7)
    bst.insert(0)
    bst.insert(5)
    bst.insert(6)
    bst.insert(5)
    for v in bst:
        print(v)
    for v in reversed(bst):
        print(v)

    s = tree_printer(bst._root, lambda x: x.data)

    print(s)
    bst.delete(0)
    s = tree_printer(bst._root, lambda x: x.data)

    print(s)
    bst.delete(4)
    s = tree_printer(bst._root, lambda x: x.data)

    print(s)
