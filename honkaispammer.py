import pyautogui
import time
from pyautogui import *


class HonkaiSpammer:

    def spammer():
        while 1:
            if pyautogui.locateOnScreen('chatmess.png',grayscale=True,confidence=0.8) != None:
                pyautogui.moveTo(pyautogui.locateOnScreen('chatmess.png',grayscale=True,confidence=0.8));time.sleep(0.5);pyautogui.click()
                pyautogui.typewrite('!rank EN',interval=0.25);pyautogui.press('enter');print('message sent!Waiting next 480 sec.');time.sleep(480)


HonkaiSpammer.spammer()