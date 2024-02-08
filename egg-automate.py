import time
import sys
import pyautogui

window_name = 'Egg'

def focus_egg():
    eggs = pyautogui.getWindowsWithTitle(window_name)

    egg_idx = next((i for i, x in enumerate(eggs) if x.title == window_name), None)

    eggs[egg_idx].activate() if egg_idx is not None else quit_earlier() 

def quit_earlier():
    print('!!! Egg not found !!!')
    sys.exit(-1)


def run_loop():
    focus_egg()

    while 1:   
        time.sleep(0.05)

        try:
            if pyautogui.getActiveWindow().title == window_name:
                pyautogui.typewrite(' ')
        except AttributeError:
            pass

if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    run_loop()
