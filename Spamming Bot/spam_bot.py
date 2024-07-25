import time
import pyautogui

def sendMessage():
    time.sleep(4)
    text = open("shrek_latino_script.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")


sendMessage()