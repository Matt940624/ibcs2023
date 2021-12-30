# data_structures/stack.py
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class Stack:
    def __init__(self):
        self._head: Node = None
        self._length = 0
        self._iter: Node = None

    def push(self, data: int):
        # put things on the stack
        n = Node(data)
        n.next = self._head
        self._head = n
        self._length += 1

    def pop(self) -> int:
        # take things off the stack
        if self._head is None:
            return None

        tmp = self._head.data
        self._head = self._head.next
        self._length -= 1
        return tmp

    def __iter__(self):
        self._iter = self._head
        return self

    def __next__(self):
        if self._iter is None:
            raise StopIteration
        tmp = self._iter.data
        self._iter = self._iter.next
        return tmp

    def __contains__(self, data: int) -> bool:
        for d in self:
            if d == data:
                return True
        return False

    def __len__(self):
        return self._length

    def __str__(self):
        s = "["
        n = self._head
        while n is not None:
            s += f"{n.data}"
            n = n.next
            if n is not None:
                s += ", "
        s += "]"
        return s


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(10)
    s.push(6)

    for x in s:
        print(x)
    print(str(s))
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(str(s))
