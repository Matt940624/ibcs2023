# data_structures/queue.py
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class Queue:
    def __init__(self):
        self._head: Node = None
        self._tail: Node = None
        self._length: int = 0
        self._iter: Node = None

    def enqueue(self, data: int) -> None:
        n = Node(data)
        if self._tail is None:
            self._head = n
            self._tail = n
        else:
            self._tail.next = n
            self._tail = n
        self._length += 1

    def dequeue(self) -> int:
        if self._head is None:
            return None

        data = self._head.data
        self._head = self._head.next
        self._length -= 1
        # If we've dequeued the last element
        # move tail to None
        if self._head is None:
            self._tail = None
        return data

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

    def __str__(self) -> str:
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
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(f"Length:{len(q)}")
