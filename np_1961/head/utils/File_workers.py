from sys import path 
from info import username
import numpy as np

class file_workers:
    def add_url(url, file_path):
        file_start='/home/np_1961/instagram/'
        full_path=file_start+username+'/'+file_path        
        followers_txt_file=open(full_path,'a')
        followers_txt_file.write(url+'\n')
        followers_txt_file.close()

    
    def txt_file_update(file_path):
        file_start='/home/np_1961/instagram/'
        full_path=file_start+username+'/'+file_path   
        
        txt_file=open(full_path).readlines()       
        txt_file=[line.split('\n')[0] for line in txt_file]
        txt_file=[line for line in txt_file if line]
        txt_file=np.array(list(set(txt_file)))
        
        file_workers.txt_file_init_(file_path=file_path)
        for url in txt_file:
            file_workers.add_url(url=url, file_path=file_path)
        return txt_file
        
    def new_folder(name):
        if exists(name):
            print(name +' folder success')
        else:
            mkdir(name)
    
    def txt_file_init_(file_path):
        file_start='/home/np_1961/instagram/'
        full_path=file_start+username+'/'+file_path        
        file=open(full_path, 'w')
        file.close()
    
    def del_url_in_txt_file(url,file_path):
        lines=file_workers.txt_file_update(file_path=file_path)
        lines=[line for line in lines if line !=url]

        
        file_workers.txt_file_init_(file_path=file_path)
        for line in lines:
            file_workers.add_url(url=line,
                                file_path=file_path)
        
