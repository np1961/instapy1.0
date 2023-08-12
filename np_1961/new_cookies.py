#all importing framework
from sys import path
#my             -----------
#profile date
path.append('./head/profile/')
from info import username

path.append('/home/np_1961/instagram/'+username+'/head/utils/')
path.append('/home/np_1961/instagram/'+username+'/head/')

from INSTAPY import Instapy




if __name__=='__main__':
    instapy=Instapy(cookies=False)
else:
    print('ERRORS IN PYTHON')
    pass
