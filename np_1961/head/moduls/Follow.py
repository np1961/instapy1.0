

from time import sleep
from sys import path


from Finder import finder
from Time import time_random
from Params import preprocessor_params


def follow(instapy ,activate_param):
    
    
    nickname_url_to_scan,scrolls,limite,time_sleep=activate_param
     
    follow_success=0

    links=instapy.scanner_profile_followers(
                                nickname_url_to_scan=nickname_url_to_scan, 
                                 scrolls=scrolls, 
                                 scan_by='followers')
    
    armenian_links=finder.find_links_geolocation(links=links)
    
    for nickname_url in armenian_links:
        
        if limite:
            limite-=1
            follow_success+=1
            instapy.follow_one_nickname(nickname_url=nickname_url)
            sleep(time_random(time_sleep))
        else:
            break
            
        
    
    instapy.go_website()
    print('follow success ->',follow_success )
    return instapy
