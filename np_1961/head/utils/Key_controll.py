
from pynput.keyboard import Key as KEYS
from pynput import keyboard
from time import sleep
import pyautogui

generator_keyboard = keyboard.Controller()

class key_controll:
    def tab_click(rangers=1):
        sleep(2)
        rangers=range(rangers)
        for tab in rangers:
            sleep(0.5)
            generator_keyboard.press(KEYS.tab)
            generator_keyboard.release(KEYS.tab)
            sleep(0.2)
        
        
    def escape_click():
        generator_keyboard.press(KEYS.esc)
        sleep(1)
        generator_keyboard.release(KEYS.esc)
        sleep(1)
        
    def enter_click():
        generator_keyboard.press(KEYS.enter)
        generator_keyboard.release(KEYS.enter)
        sleep(1)
        
    def right_click():
        pyautogui.press('right')
        sleep(2)
        
    def login_presses(username,password):
        pyautogui.write(username, interval=0.2)
        pyautogui.press('tab')
        pyautogui.write(password, interval=0.2)
        pyautogui.press('enter')
        
    def paste_and_enter():
        pyautogui.hotkey('ctrl','V')
        pyautogui.press('enter')
        
    
        
