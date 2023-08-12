

from pynput import mouse 
from pynput.mouse import Button as MOUSE_KEYS
from time import sleep
from Norm_generate import norm_method



generator_mouse = mouse.Controller()


from pynput import mouse 
from pynput.mouse import Button as MOUSE_KEYS
from time import sleep
from Norm_generate import norm_method
from Time import time_random


generator_mouse = mouse.Controller()


class mouse_controll:
    def cirle_run():
        cirle_cordinate=[  [462, 732],
                           [489, 736],
                           [504, 724],
                           [508, 704],
                           [510, 685],
                           [504, 666],
                           [478, 645],
                           [458, 644],
                           [440, 650],
                           [425, 666],
                           [420, 698],
                           [423, 712],
                           [439, 738],
                           [464, 743]]
        
        for cordinate in cirle_cordinate:
            sleep(time_random(0.05))
            generator_mouse.position=cordinate
    
    def cirle_combo(rangers):
        [mouse_controll.cirle_run() for ranger in range(rangers)]
        
    def random_pixels():
        sleep(1)
        generator_mouse = mouse.Controller()
        generator_mouse.position=[norm_method(100,1000),norm_method(100,1000)]


    
    def scrollin(rangers=None, value=-10):
        if rangers:
            generator_mouse.position=(599, 607)
            for ranger in range(rangers):
                sleep(1)
                generator_mouse.scroll(0,value)
                sleep(1)
                generator_mouse.scroll(0,2)
                sleep(1)
                generator_mouse.scroll(0,value)
                
                
            
        else:
            generator_mouse.position=(599, 607)
            sleep(1)
            generator_mouse.scroll(0,-1)
            sleep(1)
            generator_mouse.scroll(0,-1)
            sleep(1)
            generator_mouse.scroll(0,-1)
            sleep(1)
            
    def controll_click(cordinate, click=1, standart=1):
        generator_mouse.position=cordinate
        sleep(standart)
        generator_mouse.click(MOUSE_KEYS.left, click)
        sleep(standart)
