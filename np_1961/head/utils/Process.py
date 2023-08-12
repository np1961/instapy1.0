from alive_progress import alive_it
from time import sleep

def loading(time_sleep=0.009,values=100):
    values=range(values)
    for process in alive_it(values):
        sleep(time_sleep)

