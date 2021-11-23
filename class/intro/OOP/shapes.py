#  OOP/shapes.py
from math import pi


class Circle:

    def __init__(self, r: float):
        """
        Constructor for a circle

        Args:
            r: the radius of the circle
        """
        self._r = r
        print(f"This is the constructor: r: {r}")

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r: float):
        print("r.setter")
        if r <= 0:
            raise ValueError("radius must be > 0")
        self.r = r

    @property
    def circumference(self):
        return self._r * pi * 2

    @property
    def area(self):
        return self._r**2 * pi

    def __str__(self):
        return (f"{self._r}\tCircumeference: {self.circumference}\tarea:{self.area}")

    def __gt__(self, other):
        if type(other) > Circle:
            return self._r > other._r
        if type(other) == float or type(other) == int:
            return self.area > other

        # IF the other object has an area member
        area = getattr(other, "area", None)
        if area is not None:
            return self. area > other.area
        return False

    def __lt__(self, other):
        if type(other) < Circle:
            return self._r < other._r
        if type(other) == float or type(other) == int:
            return self.area < other

        # IF the other object has an area member
        area = getattr(other, "area", None)
        if area is not None:
            return self. area < other.area
        return False

    def __eq__(self, other):
        if type(other) == Circle:
            return self._r == other._r
        if type(other) == float or type(other) == int:
            return self.area == other

        # IF the other object has an area member
        area = getattr(other, "area", None)
        if area is not None:
            return self. area == other.area
        return False


class Rectangle:

    def __init__(self, h: float, w: float):
        self._h = h
        self._w = w

    @property
    def w(self):
        return self._w

    @property
    def h(self):
        return self._h

    @w.setter
    def w(self, w: float):
        if w <= 0:
            raise ValueError("Width must be larger than 0")
        self.w = w

    @h.setter
    def h(self, h: float):
        if h <= 0:
            raise ValueError("Height must be larger than 0")
        self.h = h

    @property
    def perimeter(self):
        return (self.w + self.h)*2

    @property
    def area(self):
        return self.h * self.w

    def __str__(self):
        return(
            f"""
            Width: {self.w}
            Height: {self.h}
            Area: {self.area}
            Perimeter: {self.perimeter}
            """
        )


def main():
    c = Circle(5)
    print(c)
    c2 = Circle(10)

    if c > c2:
        print("c is larger thna c2")
    else:
        print("c2 is larger than c")

    d = Rectangle(5, 4)
    print(d)
    # print(f"{c.r}\tCircumeference: {c.circumference}\tarea:{c.area}")


if __name__ == "__main__":
    main()
