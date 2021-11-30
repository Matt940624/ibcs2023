# enigma.py
from typing import Any
import numpy.random as random

ENCODING = "UTF-8"
PERMUTATION_SIZE = 8


class Enigma:
    def __init__(self, seed: Any):
        random.seed(seed)

    def encipher(self, val: int) -> int:
        pass


class Plugboard:
    def __init__(self) -> None:
        pass

    def encipher_forwards(self, val: int) -> int:
        pass

    def encipher_backwards(self, val: int) -> int:
        pass


class Rotor:
    def __init__(self) -> None:
        pass

    def set_position(self, position):
        pass

    def rotate(self):
        pass

    def rotate_next(self) -> bool:
        pass

    def encipher_forwards(self, val: int) -> int:
        pass

    def encipher_backwards(self, val: int) -> int:
        pass


class Reflector:
    def __init__(self) -> None:
        self._permutations = [i for i in range(0, PERMUTATION_SIZE)]
        tmp_vals = [i for i in range(0, PERMUTATION_SIZE)]
        for idx, val in enumerate(self._permutations):
            if idx == val:
                rnd = idx
                while idx == rnd:
                    # Choose a random value from temp_vals
                    rnd = random.choice(tmp_vals)
                # idx points to rnd
                # rnd points to idx
                self._permutations[idx] = rnd
                self._permutations[rnd] = idx
                # remove idx and rnd from tmp values
                # so they can't be used again
                tmp_vals.remove(idx)
                tmp_vals.remove(rnd)

    def encipher(self, val: int) -> int:
        return self._permutations[val]


if __name__ == "__main__":
    r = Reflector()
    print(r._permutations)
