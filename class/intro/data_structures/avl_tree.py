# data_structures/binary_tree.py

from typing import Callable
from os import linesep


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.height: int = 0
        self.right: Node = None
        self.left: Node = None


class AVLTree:
    def __init__(self) -> None:
        self._root: Node = None
        # for easy interpretation in __len__(self)
        self._length: int = 0

    def insert(self, data: int) -> None:
        self._root = self._insert(data, self._root)

    def _insert(self, data: int, root: Node) -> Node:
        # root is the root of a subtree.
        # any internal node that has a subtree below it
        if root is None:
            # if it's the first node
            self._length += 1
            return Node(data)

        if data < root.data:
            # recursive call
            root.left = self._insert(data, root.left)
        else:
            root.right = self._insert(data, root.right)

        return self._rebalance(root)

    def height(self) -> int:
        return self._root.height

    def _height(self, root: Node):
        if root is None:
            return -1

        # find the greatest height from root.left and root.right
        # needs to +1
        root.height = max(self._height(root.left),
                          self._height(root.right)) + 1
        return root.height

    def _get_balance(self, root: Node = None) -> int:
        if root is None:
            return 0
        else:
            return self._height(root.left)-self._height(root.right)

    def _rebalance(self, root: Node = None) -> int:
        if root is None:
            return None
        balance = self._get_balance(root)
        left_balance = self._get_balance(root.left)
        right_balance = self._get_balance(root.right)

        if balance > 1 and left_balance >= 0:
            return self._rotate_right(root)
        if balance > 1 and left_balance < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance < -1 and right_balance <= 0:
            return self._rotate_left(root)
        if balance < -1 and right_balance > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)
        return root

    def _rotate_left(self, root: Node) -> Node:
        new_root = root.right
        left_subtree = new_root.left

        new_root.left = root
        root.right = left_subtree
        self._height(new_root)
        return new_root

    def _rotate_right(self, root: Node) -> Node:
        new_root = root.left
        right_subtree = new_root.right

        new_root.right = root
        root.left = right_subtree
        self._height(new_root)
        return new_root

    def __len__(self):
        return self._length

    def __iter__(self):
        def inorder_generator(root: Node) -> int:
            # left -> root -> right
            if root.left:
                yield from inorder_generator(root.left)
            yield root.data
            if root.right:
                yield from inorder_generator(root.right)

        return inorder_generator(self._root)

    def __reversed__(self):
        def reverseorder_generator(root: Node) -> int:
            # left -> root -> right
            if root.right:
                yield from reverseorder_generator(root.right)
            yield root.data
            if root.left:
                yield from reverseorder_generator(root.left)

        return reverseorder_generator(self._root)

    def delete(self, data: int) -> None:
        self._delete(data, self._root)

    def _delete(self, data: int, root: Node) -> Node:
        if root is None:
            return None
        # if data is less than current root data
        # traverse down left subtree

        if data < root.data:
            root.left = self._delete(data, root.left)

        # if data is greater than current root data
        # traverse down right subtree

        elif data > root.data:
            root.right = self._delete(data, root.right)

        # if data is the same as the current root data
        # delete this node while preserving subtrees
        else:
            self._length -= 1

            """also takes care when there's no children"""
            # If there is only a right subtree
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            # If there is only a left subtree
            if root.right is None:
                tmp = root.left
                root = None
                return tmp

            # node has two children
            # choose the smallest in-order successor
            tmp = self._min_node(root.right)
            root.data = tmp.data
            root.right = self._delete(tmp.data, root.right)

        return root

    def _min_node(self, root: Node) -> Node:
        # looks until there is no left so to knwo that there is no more successor
        if root.left is not None:
            return self._min_node(root.left)
        return root

    def __contains__(self, data: int) -> bool:
        root = self._root
        while root:
            if root == data:
                return True
            elif data < root.data:
                root = root.left
            else:
                root = root.right
        return False

    def max(self) -> int:
        if self._root is None:
            return None
        node = self._root
        while node.right is not None:
            node = node.right
        return node.data

    def min(self) -> int:
        if self._root is None:
            return None
        node = self._root
        while node.left is not None:
            node = node.left
        return node.data


def tree_printer(root: Node, data_func: Callable, width: int = 64):
    elem_cnt = 2 ** (root.height + 1) - 1
    elms = [None] * elem_cnt

    def flatten(root: Node, idx: int = 0):
        # pull some data out
        elms[idx] = data_func(root)
        if root.left:
            flatten(root.left, idx * 2 + 1)
        if root.right:
            flatten(root.right, idx * 2 + 2)
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
            level_width = level_width // 2
            level += 1
            end += 2 ** level

    return s


if __name__ == "__main__":
    bst = AVLTree()

    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1234)
    bst.insert(6)
    bst.insert(5)
    bst.insert(5)

    for v in reversed(bst):
        print(v)

    # def get_data(x):
    #     return x.data
    s = tree_printer(bst._root, lambda x: x.data)
    print(s)

    bst.delete(1234)
    bst.delete(5)
    s = tree_printer(bst._root, lambda x: x.data)
    print(s)

    print(f"Min: {bst.min()}")
    print(f"Max: {bst.max()}")
    print(f"Contains 3: {3 in bst}")
    print(f"Contains 10: {10 in bst}")
