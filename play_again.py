import mss
import cv2
import numpy as np
import pyautogui
import time


MATCH_THRESHOLD = 0.4
with mss.mss() as sct:
    while True:
        try:
            click_location = pyautogui.center(pyautogui.locateOnScreen("play_again.png"))
            click_location_x, click_location_y = click_location
            pyautogui.click(click_location_x - 1000, click_location_y - 950)
        except: 
            pass