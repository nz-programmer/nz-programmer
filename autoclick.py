import time
import pyautogui
import keyboard
from multiprocessing import Process
keyboard.is_pressed('q')
a = 0
time.sleep(5)


def bot1():
    while a != 10000 or keyboard.is_pressed('q'):
        print("ok")
        pyautogui.leftClick()
        if keyboard.is_pressed('q'):
            exit()

def bot2():
    while a != 10000 or keyboard.is_pressed('q'):
        print("nee")
        pyautogui.leftClick()
        time.sleep(0.01)
        if keyboard.is_pressed('q'):
            exit()

time.sleep(5)
if __name__ == '__main__':
    p1 = Process(target=bot1)
    p1.start()
    p2 = Process(target=bot2)
    p2.join()

