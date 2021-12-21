# main.py
from typing import Any
import numpy.random as random
# import random

ENCODING = "UTF-8"
PERMUTATION_SIZE = 256  # because bytes can only store to 256
ROTOR_DIMS = (10, 20)


class Enigma:
    def __init__(self, seed: Any):
        random.seed(seed)
        self._plugboard = Plugboard()
        self._rotors = []
        self._reflector = Reflector()
        num_rotors = random.randint(ROTOR_DIMS[0], ROTOR_DIMS[1])
        for _ in range(0, num_rotors):  # this determines how many rotors
            self._rotors.append(Rotor())

    def encipher(self, val: int) -> int:  # we're going to treat those bytes like they're integers
        # Pass one way through the rotors
        cipher = self._plugboard.encipher_forwards(val)

        # go through each of our rotor
        for idx, rotor in enumerate(self._rotors):
            # Always rotate first rotor
            if idx == 0:
                rotor.rotate()
            # see if the rotor in front of it says that it's time to rotate
            elif self._rotors[idx - 1].rotate_next():
                rotor.rotate()
            cipher = rotor.encipher_forwards(cipher)

        cipher = self._reflector.encipher(cipher)

        for rotor in self._rotors[::-1]:  # -1 here is the backward step
            cipher = rotor.encipher_backwards(cipher)

        cipher = self._plugboard.encipher_backwards(cipher)

        return cipher


class Plugboard:
    def __init__(self):
        self._wires = [i for i in range(PERMUTATION_SIZE)]
        swapped = []
        for idx, val in enumerate(self._wires):
            if idx not in swapped and random.randint(0, 9) <= 5:
                # each wire will have a 60% chance to be swapped
                # choose a random location to swapped
                # if value is already swapped, then don't swap
                loc = random.randint(0, len(self._wires) - 1)
                if loc not in swapped:
                    tmp = self._wires[loc]
                    # set that the value of where we're at
                    self._wires[loc] = val
                    # set the previous value to the one we chose
                    self._wires[idx] = tmp
                    swapped.insert(0, idx)
                    swapped.insert(0, loc)

# get index return value
    def encipher_forwards(self, val: int) -> int:
        cipher = self._wires[val]
        return cipher

# undoing encipher forwards, get value return index
    def encipher_backwards(self, val: int) -> int:
        cipher = self._wires.index(val)
        return cipher

    def _str_(self):
        s = "Plugboard: \n"
        for idx, val in enumerate(self._wires):
            s += f"{idx} <-> {val}\n"

        return s


class Rotor:
    def __init__(self):
        # each will rotate when the previous one finish rotating
        self._rotor_pos = 0
        self._rotate_next_pos = random.randint(0, PERMUTATION_SIZE - 1)
        self._wires = [i for i in range(0, PERMUTATION_SIZE)]
        random.shuffle(self._wires)
        # we need to move data around in a circular way since the selections were random
        self.set_position(random.randint(0, PERMUTATION_SIZE - 1))

    def set_position(self, position):
        # looking at where we want to be and where we are now
        change = self._wires.index(position) - self._rotor_pos
        self._rotor_pos = position
        # grabs the end and moves it to the front
        self._wires = self._wires[change:] + self._wires[:change]

    def rotate(self):
        # set to new position, now we need to rotate our data
        self._rotor_pos = (self._rotor_pos + 1) % PERMUTATION_SIZE
        # grab everything from index one to the end. this moves index zero to the back
        self._wires = self._wires[1:] + self._wires[:1]

    def rotate_next(self):
        return self._rotor_pos == self._rotate_next_pos

    def encipher_forwards(self, val: int) -> int:
        cipher = self._wires[val]
        return cipher

    def encipher_backwards(self, val: int) -> int:
        cipher = self._wires.index(val)
        return cipher

    def __str__(self) -> str:
        s = f"Rotor\n\t{self._wires}\n\tRotor Position: {self._rotor_pos}\n\tRotate Next Position: {self._rotate_next_pos}"


class Reflector:
    def __init__(self):
        self._permutations = [i for i in range(0, PERMUTATION_SIZE)]
        tmp_vals = [i for i in range(0, PERMUTATION_SIZE)]
        # shuffle these values so that the index just go to another value
        for idx, val in enumerate(self._permutations):
            if idx == val:
                rnd = idx
                while idx == rnd:  # because there's a possibility that the two would be the same, then the numebr doesn't actually change
                    # Choose a random value from temp_vals
                    rnd = random.choice(tmp_vals)
                self._permutations[idx] = rnd
                self._permutations[rnd] = idx
                # remove idx and rnd from temp values
                # so they can't be used again
                tmp_vals.remove(idx)
                tmp_vals.remove(rnd)

                # However, this would only really work for even number

    def encipher(self, val: int) -> int:
        return self._permutations[val]


if __name__ == "__main__":
    # r = Reflector()
    # print(r._permutations)
    # p = Plugboard()
    # print(p)

    # r = Rotor()
    # print(r)

    e = Enigma(100)
    cipher = e.encipher(5)
    print(cipher)
    e = Enigma(100)
    cipher = e.encipher(cipher)
    print(cipher)
