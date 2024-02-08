"""Script providing a simple auto clicker for the game Egg."""

import time
import sys
import pyautogui

WINDOW_NAME = 'Egg'

def focus_egg():
    """Function that looks for the game window and then focus on it."""
    eggs = pyautogui.getWindowsWithTitle(WINDOW_NAME)

    egg_idx = next((i for i, x in enumerate(eggs) if x.title == WINDOW_NAME), None)

    if egg_idx is not None:
        eggs[egg_idx].activate()
    else:
        quit_earlier()


def quit_earlier():
    """Function that terminates the execution if Egg is not running."""
    print('!!! Egg not found !!!')
    sys.exit(-1)


def run_loop():
    """Function that runs an infinite loop pressing SPACE on Egg."""
    focus_egg()

    while 1:
        time.sleep(0.05)

        try:
            if pyautogui.getActiveWindow().title == WINDOW_NAME:
                pyautogui.typewrite(' ')
        except AttributeError:
            pass

if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    run_loop()
