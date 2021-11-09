from typing import Type


def user_input(prompt: str) -> int:
    try:
        return int(input(prompt))
    except(ValueError, TypeError):
        return -1


def start():
    print(
        """
        It's a dark and stormy night and you believe that you're home alone.
        You are sitting on your bed watching Youtube videos.
        You hear a sound coming from the other room. 
        What do you do?

        1. turn up the volume
        2. listen carefully for the sound
        3. investigate the sound
        """
    )
    choice = -1
    while choice < 1 or choice > 3:
        choice = user_input("make a goddamn choice: ")

        if choice == 1:
            volume()
        elif choice == 2:
            listen()
        elif choice == 3:
            investigate()
        else:
            print("please choose 1, 2 ,3  you idiot")


def volume():
    print(
        """
        u ignore killer, she comes in you room and is prepared to butcher you like the pig u are
        """
    )


def listen():
    print("""
    you listen carefully to the sounds in your house.
    After a few minutes you hear a strange noise coming from the other room
    you believe someone is moving in that room.

    what do you want to do?

    1. lock your door
    2. investigate the inturder
    3. turn the volume even louder
    """)
    choice = -1
    while choice < 1 or choice > 3:
        choice = user_input("make a choice:")

    if choice == 1:
        lock_door()
    elif choice == 2:
        investigate()
    elif choice == 3:
        volume()
    else:
        print("please choose 1, 2, 3")


def investigate():
    print("""
    haha you died
    """)


def lock_door():
    print("""
    haha you died
    """)


if __name__ == '__main__':
    start()
