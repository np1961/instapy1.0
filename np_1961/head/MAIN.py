

#python       ----------
import os
from sys import path
from time import time

#conda        ----------
import numpy as np
from pandas import DataFrame

#head         ----------
from INSTAPY import Instapy

#moduls       ----------
from Like import like_by_following
from Like import like_by_tags
from Follow import follow
from Story import story
from Unfollow import unfollow
from Comments import comments


#utils for organization working
              
from Print import printer_sell
from Process import loading
from Questions import questions
from Params import preprocessor_params
from Time import time_calculator
from Emoji import get_menu_emoji



#processing_all_in_main |||
def main():

    emojize=get_menu_emoji()
    clear_values=os.system('clear')
    printer_sell(menu_display=True)
    start=time()
    
    moduls=[follow, unfollow, like_by_tags, like_by_following, story, comments]
    activate_params,indicators =questions.main_stream()
    clear_values=os.system('clear')
    printer_sell(menu_display=True)

    instapy=Instapy()
    for index, column in enumerate(activate_params):
        
        if indicators[index]:
            activate_param=preprocessor_params(series=activate_params[column])

            try:
                instapy=moduls[index](instapy=instapy,
                           activate_param=activate_param)

                print(column, 'Finished !!! ')
            except:
                print('this functions -> ', column, ' errors')
                
            
            
            
            
        else:
            print(column, ' is None !!!')
            print('And we continue !!! ')
            
        printer_sell()
        loading()
        activate_params[column]=emojize[index]
        print(activate_params)
        
    if all(activate_params):
        print(' || EXIT ALL CONFLICTING PROCESSES !!! ||')
        loading(0.029)
        printer_sell()
        print('||| ALL PROCESSES WERE SUCCESSFULLY COMPLETED !!! ')
        loading()
        instapy.exit_and_saving_cookies()
        time_calculator(start=start)
        printer_sell(menu_display=True)
        printer_sell(menu_display=True)

