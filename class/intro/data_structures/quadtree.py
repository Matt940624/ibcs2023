from collections import namedtuple
from typing import List


Coord = namedtuple("Coord", ["x", "y"])


class Quad:
    def __init__(self, right: int, bottom: int):
        self.ne = None
        self.se = None
        self.nw = None
        self.sw = None
        self.right = right
        self.bottom = bottom
        self.children: List[Coord] = []

    def add(self, child: Coord):
        pass

    def divide(self):
        """
        Divides this quad into four equal quads
        """
        pass

    def __len__(self):
        return len(self.children)

    def __str__(self):
        cd = [f"({c.x}, {c.y})" for c in self.children]

        return f"""Quad ({self.right}, {self.bottom}): {len(self.children)}
    {', '.join(cd)}
NW:{self.nw}
NE:{self.ne}
SW:{self.sw}
SE:{self.se}
"""


class QuadTree:
    def __init__(self, right: int, bottom: int, max_cap: int = 5):
        self._max_cap = max_cap
        self._root = Quad(right=right, bottom=bottom)

    def add(self, child: Coord):
        pass

    def __str__(self):
        return str(self._root)


if __name__ == "__main__":
    qt = QuadTree(1024, 1024)

    qt.add(Coord(256, 256))
    qt.add(Coord(768, 256))
    qt.add(Coord(256, 768))
    qt.add(Coord(768, 768))
    qt.add(Coord(256, 100))
    qt.add(Coord(256, 200))
    qt.add(Coord(256, 300))
    qt.add(Coord(256, 400))
    qt.add(Coord(100, 400))
    qt.add(Coord(200, 400))
    qt.add(Coord(300, 400))
    qt.add(Coord(400, 400))
    print(qt)
    print("─" * 50)
