# context.py
import curses

MENU = "menu"
OPTIONS = "options"
PROMPT = "prompt"
SCREEN = "screen"
POS = "pos"
TEXT = "text"
CALLBACK = "callback"
STATUS_FORMAT = "          |Key: {:>5} Active: {:>3} "


def create_menu_item(pos: int, text: str, callback: callable):
    menu_item = {POS: pos, TEXT: text, CALLBACK: callback}
    return menu_item


def create_menu(prompt: str, options: list) -> dict:
    menu = {
        PROMPT: prompt,
        OPTIONS: options
    }
    return menu


def draw_menu(ctx: dict, menu: dict) -> callable:
    # curses screen to draw to
    s = ctx[SCREEN]
    # menu options we can choose from
    o = menu[OPTIONS]
    # make sure options are in order we want
    o.sort(key=lambda x: x[POS])
    # the last key to be pressed
    key = 0
    # the current index of the active option
    active = 0

    h, w = s.getmaxyx()
    while key != 27:
        # handlekey presses
        # if key is down key
        if key == 456 or key == curses.KEY_DOWN:
            active = (active+1) % len(o)
        # if key is up key
        elif key == 450 or key == curses.KEY_UP:
            active = (active-1) % len(o)
        # if key is enter
        elif key == 10 or key == curses.KEY_ENTER:
            return o[active][CALLBACK]

        s.clear()
        # Do something here later
        s.addstr(2, 3, menu[PROMPT])

        opt_height = 5

        for idx, opt in enumerate(o):
            if idx == active:
                s.attron(curses.color_pair(3))
                s.addstr(opt_height+idx, 8, opt[TEXT])
                s.attroff(curses.color_pair(3))
            else:
                s.addstr(opt_height+idx, 8, opt[TEXT])

        # Draw status bar
        status_string = STATUS_FORMAT.format(key, active)
        s.attron(curses.color_pair(4))
        s.addstr(h - 1, 0, status_string)
        s.addstr(h - 1, len(status_string), " " * (w-len(status_string)-1))
        s.attroff(curses.color_pair(4))

        s.move(h-1, 1)
        s.refresh()
        key = s.getch()


def init() -> dict:
    context = {}
    context[SCREEN] = curses.initscr()
    context[SCREEN].clear()
    context[SCREEN].keypad(1)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

    return context
    # screen.clear()
    # h, w = screen.getmaxyx()
    # c = 1
    # screen.attron(curses.color_pair(c))
    # screen.addstr(3, 3, "Test")
    # screen.attroff(curses.color_pair(c))

    # screen.move(h-1, 1)
    # screen.refresh()
    # key = screen.getch()


if __name__ == '__main__':
    ctx = init()
    menu = {
        PROMPT: "This is the prompt",
        OPTIONS: [
            create_menu_item(0, "Option 1", None),
            create_menu_item(1, "Option 2", None),
            create_menu_item(2, "Option 3", None),
            create_menu_item(3, "Option 4", None),

        ]
    }
    draw_menu(ctx, menu)
