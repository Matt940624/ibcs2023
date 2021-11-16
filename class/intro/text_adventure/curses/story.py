# story.py
import context as c


def start(ctx):
    prompt = "I'm the starter prompt. I start the story"
    options = []
    options.append(c.create_menu_item(1, "START", start))
    options.append(c.create_menu_item(2, "EXIT", None))
    options.append(c.create_menu_item(3, "Start", start))
    options.append(c.create_menu_item(4, "Quit", quit()))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def start(ctx):
    prompt = "I'm the starter prompt. I start the story"
    options = []
    options.append(c.create_menu_item(1, "", start))
    options.append(c.create_menu_item(2, "", None))
    options.append(c.create_menu_item(3, "", start))
    options.append(c.create_menu_item(4, "Quit", quit()))

    menu = c.create_menu(prompt, options)
    return c.draw_menu(ctx, menu)


def quit():
    prompt = "Are "
    options = []


def main():
    ctx = c.init()
    cb = start(ctx)
    while cb != None:
        cb = cb(ctx)


if __name__ == "__main__":
    main()
