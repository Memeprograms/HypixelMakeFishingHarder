import random
import math
import time
import pyautogui
import keyboard

while True:

    randomnumber = random.randint(1,2000)

    if randomnumber == range(1,50):
        pyautogui.click(button="right")
        print("Right clicked")

    if randomnumber == range(50,75):
        pyautogui.click("s")
        print("S clicked")

    if randomnumber == range(75,100):
        pyautogui.click("w")
        print("W clicked")


    if randomnumber == 169:
        pyautogui.keyDown("alt")
        pyautogui.keyDown("f4")
        pyautogui.keyUp("alt")
        pyautogui.keyUp("f4")
        print("Game closed")


    def cancel():
        randomnumber = 0
    
    keyboard.is_pressed("k", cancel())

    if randomnumber == 0:
        break

    time.sleep(1)
