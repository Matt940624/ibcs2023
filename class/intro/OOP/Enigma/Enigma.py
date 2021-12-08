# enigma.py
from typing import Any
import numpy.random as random

ENCODING = "UTF-8"
PERMUTATION_SIZE = 256
ROTOR_DIMS = (10, 20)


class Enigma:
    def __init__(self, seed: Any):
        random.seed(seed)
        self._plugboard = Plugboard()
        self._rotors = []
        self._reflector = Reflector()
        num_rotors = random.randint(ROTOR_DIMS[0], ROTOR_DIMS[1])
        for _ in range(0, num_rotors):
            self._rotors.append(Rotor())

    def encipher(self, val: int) -> int:
        # pass one way through the rotors
        cipher = self._plugboard.encipher_forwards(val)
        for idx, rotor in enumerate(self._rotors):
            # always rotate first rotor
            if idx == 0:
                rotor.rotate()
            elif self._rotors[idx-1].rotate_next():
                rotor.rotate()
            cipher = rotor.encipher_forwards(cipher)

        cipher = self._reflector.encipher(cipher)
        for rotor in self._rotors[::-1]:
            cipher = rotor.encipher_backwards(cipher)
        cipher = self._plugboard.encipher_backwards(cipher)
        return cipher


class Plugboard:
    def __init__(self) -> None:
        self._wires = [i for i in range(PERMUTATION_SIZE)]
        swapped = []
        for idx, val in enumerate(self._wires):
            if idx not in swapped and random.randint(0, 9) <= 5:
                # each wire will have a 60% chance of being swapped
                # choose a random location to be swapped
                loc = random.randint(0, len(self._wires)-1)
                if loc not in swapped:
                    tmp = self._wires[loc]
                    self._wires[loc] = val
                    self._wires[idx] = tmp
                    swapped.insert(0, idx)
                    swapped.insert(0, loc)

    def encipher_forwards(self, val: int) -> int:
        cipher = self._wires[val]
        return cipher

    def encipher_backwards(self, val: int) -> int:
        cipher = self._wires.index(val)
        return cipher

    def __str__(self):
        s = "Plugboard: \n"
        for idx, val in enumerate(self._wires):
            s = s + f"{idx}<->{val}\n"
        return s


class Rotor:
    def __init__(self) -> None:
        self._rotor_pos = 0
        self._rotate_next_pos = random.randint(0, PERMUTATION_SIZE-1)
        self._wires = [i for i in range(0, PERMUTATION_SIZE)]
        random.shuffle(self._wires)
        self.set_position(random.randint(0, PERMUTATION_SIZE-1))

    def set_position(self, position):
        change = self._wires.index(position) - self._rotor_pos
        self._rotor_pos = position
        self._wires = self._wires[change:]+self._wires[:change]

    def rotate(self):
        self._rotor_pos = (self._rotor_pos + 1) % PERMUTATION_SIZE
        self._wires = self._wires[1:]+self._wires[:1]

    def rotate_next(self) -> bool:
        return self._rotor_pos == self._rotate_next_pos

    def encipher_forwards(self, val: int) -> int:
        cipher = self._wires[val]
        return cipher

    def encipher_backwards(self, val: int) -> int:
        cipher = self._wires.index(val)
        return cipher

    def __str__(self):
        s = f"Rotor\n\t{self._wires}\n\tRotor Position: {self._rotor_pos}\n\tRotate Next Position: {self._rotate_next_pos}"
        return s


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

    p = Plugboard()
    print(p)

    r = Rotor()
    print(r)

    e = Enigma(100)
    cipher = e.encipher(5)
    print(cipher)
    e = Enigma(100)
    cipher = e.encipher(cipher)
    print(cipher)
