from time import sleep
import pyautogui

def menu_controll():
    sleep(1)
    pyautogui.hotkey('winleft', 'left')
    sleep(1)
    pyautogui.hotkey('winleft', 'right')
    
