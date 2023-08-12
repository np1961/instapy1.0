from time import sleep
from Time import time_random

def story(instapy,activate_param):

    like_procent,rangers,stories,time_sleep=activate_param
    
    for ranger in range(rangers):
        instapy.all_stories_veow(stories=stories,
                             like_procent=like_procent/100)
        
        sleep(time_random(time_sleep))
        
    return instapy
