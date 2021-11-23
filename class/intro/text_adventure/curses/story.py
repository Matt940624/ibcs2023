# story.py

import context as c


def start(ctx):
    prompt = "I'm the starter prompt. I start the story"
    options = []
    options.append(c.create_menu_item(1, "START", start1))
    options.append(c.create_menu_item(2, "EXIT", None))
    options.append(c.create_menu_item(3, "Start", start1))
    options.append(c.create_menu_item(4, "Quit", quit))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def start1(ctx):
    prompt = """There is a cave uphead of this winding pathway. An eerie glow is emitting from the cave entrence.
        The entrance is half covered with moss and algae indicating that it has been quite some time since
        someone has visited.
        What do you do?"""
    options = []
    options.append(c.create_menu_item(1, "Run Away", run_away))
    options.append(c.create_menu_item(
        2, "Approach the cave entrance", approach))
    options.append(c.create_menu_item(3, "Call a friend", call))
    options.append(c.create_menu_item(4, "Quit", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def quit(ctx):
    prompt = "Are you sure you wanna quit "
    options = []
    options.append(c.create_menu_item(1, "Yes", None))
    options.append(c.create_menu_item(2, "No", start()))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def run_away(ctx):
    prompt = """
        Cry sad boohoo uwuwuwuw
        """
    options = []
    options.append(c.create_menu_item(
        1, "Cry cause you got a 2 in Jared's", None))
    options.append(c.create_menu_item(2, "Cry cause yo momma fat", None))
    options.append(c.create_menu_item(
        3, "Cry cause your dad divorced your mom", None))
    options.append(c.create_menu_item(4, "Cry cause nobody loves you", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def approach(ctx):
    prompt = """
    You arrive at the enterence, you find the moss is blockng the main enterence as well as a stone plate carved with words.
    what do you want to do?"""
    options = []
    options.append(c.create_menu_item(1, "Run Away", run_away))
    options.append(c.create_menu_item(2, "Knife", knife))
    options.append(c.create_menu_item(3, "Enter", enter))
    options.append(c.create_menu_item(4, "Quit", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def knife(ctx):
    prompt = """You stab youself with knife. You cry."""
    options = []
    options.append(c.create_menu_item(1, "Cry cause you adopted", None))
    options.append(c.create_menu_item(2, "Cry cause you fat", None))
    options.append(c.create_menu_item(
        3, "Cry cause your mom divorced your dad", None))
    options.append(c.create_menu_item(4, "Cry cause all of the above", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def enter(ctx):
    prompt = """You stab youself with knife. You cry."""
    options = []
    options.append(c.create_menu_item(1, "Cry cause you adopted", None))
    options.append(c.create_menu_item(2, "Cry cause you fat", None))
    options.append(c.create_menu_item(
        3, "Cry cause your mom divorced your dad", None))
    options.append(c.create_menu_item(4, "Cry cause nobody loves you", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def call(ctx):
    prompt = """There is a cave uphead of this winding pathway. An eerie glow is emitting from the cave entrence.
        The entrance is half covered with moss and algae indicating that it has been quite some time since
        someone has visited.
        What do you do?"""
    options = []
    options.append(c.create_menu_item(1, "Run Away", run_away))
    options.append(c.create_menu_item(
        2, "Approach the cave entrance", approach))
    options.append(c.create_menu_item(3, "Call a friend", call))
    options.append(c.create_menu_item(4, "Quit", None))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def main():
    ctx = c.init()
    cb = start(ctx)
    while cb != None:
        cb = cb(ctx)


if __name__ == "__main__":
    main()
