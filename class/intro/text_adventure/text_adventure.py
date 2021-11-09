from typing import Type


def user_input(prompt: str) -> int:
    try:
        return int(input(prompt))
    except(ValueError, TypeError):
        return -1


def start():
    print(
        """
        There is a cave uphead of this winding pathway. An eerie glow is emitting from the cave enterence.
        The enterence is half covered with moss and algae indicating that it has been quite some time since
        someone has visited.
        What do you do?

        1. Run away
        2. Approach the cave enterence
        3. Call over a friend
        """
    )
    choice = -1
    while choice < 1 or choice > 3:
        choice = user_input("make your choice: ")

        if choice == 1:
            runaway()
        elif choice == 2:
            approach()
        elif choice == 3:
            friend()
        else:
            print("please choose 1, 2 ,3")


def friend():
    print(
        """
        Your friend picks up and tells you to run away.
        What do you do?
        1. Ignore friend
        2. Trust friend
        """
    )
    choice = -1
    while choice < 1 or choice > 2:
        choice = user_input("make a choice:")

    if choice == 1:
        approach()
    elif choice == 2:
        runaway()
    else:
        print("please choose 1, 2")


def runaway():
    print(
        """
        You run away and never discovered what was in that cave. You die alone in an apartment still thinking about what would have happened if you entered the cave....
        """
    )


def approach():
    print("""
    You arrive at the enterence, you find the moss is blockng the main enterence as well as a stone plate carved with words.
    what do you want to do?

    1. take out knife to cut away moss
    2. run away
    3. scrape it with your hands
    """)
    choice = -1
    while choice < 1 or choice > 3:
        choice = user_input("make a choice:")

    if choice == 1:
        knife()
    elif choice == 2:
        runaway()
    elif choice == 3:
        enter()
    else:
        print("please choose 1, 2, 3")


def knife():
    print("""
    You put the knife away, but the enterence had completly disappeared.....leaving you in the middle of the forest.
    """)


def enter():
    print("""
    You enter the enterence, and you are horrored at the sight of 6 IB exams laid on the stone alter. Behind you the cave door shuts....
    What do you do?
    
    1. take the exams
    2. bang on the closed cave door
    3. call your friend
    """)
    choice = -1
    while choice < 1 or choice > 3:
        choice = user_input("make a choice:")

    if choice == 1:
        exam()
    elif choice == 2:
        cave()
    elif choice == 3:
        call()
    else:
        print("please choose 1, 2, 3")


def exam():
    print("""
    You take the test, you eyelids start to droop.... your head dips. You suddenly wake up and realize it was all a dream. 
    """)


def cave():
    print("""
    You are still trapped nobody hears your voice and you become desperate. Suddenly a rock falls from above and you are crushed. 
    """)


def call():
    print("""
    There is no signal. Your friend does not pick up.
    What do you do?
    1. take the exam
    2. bang on closed cave door
    """)
    choice = -1
    while choice < 1 or choice > 2:
        choice = user_input("make a choice:")

    if choice == 1:
        exam()
    elif choice == 2:
        cave()
    else:
        print("please choose 1, 2")


if __name__ == '__main__':
    start()
