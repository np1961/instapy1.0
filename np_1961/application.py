#all importing framework
import os
from sys import path
from time import time
#my             -----------
path.append('./head/profile/')
from info import username
path.append('/home/np_1961/instagram/'+username+'/head/utils/')
path.append('/home/np_1961/instagram/'+username+'/head/moduls/')
path.append('/home/np_1961/instagram/'+username+'/head/')
#head
from MAIN import main
from INSTAPY import Instapy
#utils
from Time import time_calculator
os.system('clear')





if __name__=='__main__':
    main()

else:
    print('ERRORS IN PYTHON')
    pass
