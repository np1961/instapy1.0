from random import uniform
from time import time
def time_random(seconds):
    return uniform(seconds*0.81,seconds*1.19)


def time_calculator(start):
    seconds=time()-start
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    seconds=(seconds-hours*3600-minutes*60)
    print('time process-->[ '+str(int(hours))+' :'+str(int(minutes))+' : '+str(int(seconds)) +' ]' )
    

