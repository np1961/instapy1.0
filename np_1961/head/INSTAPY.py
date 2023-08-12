#python standart ----------
from os import mkdir
from os.path import exists
from sys import path
from time import sleep
from random import randint
from random import random
from copy import deepcopy as copy
from warnings import filterwarnings as message #message 
import emoji
import pyperclip
message(action='ignore')
path.append('./profile/')
path.append('./utils/')

#my             -----------

#profile date
from info import username ,password

#utils for organization working
from File_workers import file_workers
from Norm_generate import norm_method
from Norm_generate import get_random_url
from Key_controll import key_controll
from Key_controll import generator_keyboard
from Mouse_controll import mouse_controll
from Mouse_controll import generator_mouse
from Time import time_random
from Emoji import get_positive_emoji
from Terminal import terminal_write

#pip            -----------
import pickle
from pynput import keyboard
from pynput import mouse 
from pynput.mouse import Button as MOUSE_KEYS
from pynput.keyboard import Key as KEYS

#conda          -----------
import numpy as np
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager



class INSTAPY:

    def __init__(self):
        executable_path=ChromeDriverManager().install()
        service=Service(executable_path=executable_path)
        options=Options()
        options.add_argument("window-size=965,1200")
        self.driver=webdriver.Chrome(service=service, options=options)
        self.driver.set_window_position(50,0)
        
    def go_website(self):
        self.driver.get('https://instagram.com')
        sleep(time_random(8))
        
        
    def go_profile(self, config=None, nickname_url='https://instagram.com/'+username+'/'):
        try:
            self.driver.get(nickname_url+config)
            sleep(time_random(9))
           
        except Exception:
            terminal_write(text='Error in go profile function !!!')
            
            
    
    def save_cookie(self,path='/home/np_1961/instagram/'+username+'/cookies/cookies'):
        with open(path, 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)
            terminal_write(text='Cookies generate !!! ')

            
    def load_cookie(self,path='/home/np_1961/instagram/'+username+'/cookies/cookies'):
         with open(path, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                 self.driver.add_cookie(cookie)
            self.driver.refresh()
            sleep(time_random(8))
            
            try:
                self.driver.find_element(by=By.XPATH, value="//*[text() = 'Not Now']").click()
            except Exception:
                sleep(time_random(2))
    def login(self):
        self.go_website()
        find=self.driver.find_element(by=By.NAME, value='username').click()
        key_controll.login_presses(username=username,
                                  password=password)
        sleep(time_random(8))
        
        
        try:
            self.driver.find_element(by=By.XPATH, value="//*[text() = 'Not Now']").click()
            sleep(time_random(5))
            self.driver.find_element(by=By.XPATH, value="//*[text() = 'Not Now']").click()
            sleep(time_random(5))
            
        except Exception:
            mouse_controll.controll_click(cordinate=(570, 656),
                                          click=1, standart=4)
            
            mouse_controll.controll_click(cordinate=(536, 762),
                                          click=1, standart=4)
        
        terminal_write(text='Login success -> True ')
        
        
        
        
        
    def exit(self):
        self.go_website()
        mouse_controll.cirle_combo(rangers=5)
        mouse_controll.controll_click(cordinate=(107, 1027), click=1, standart=3)
        key_controll.tab_click(rangers=6)  
        key_controll.enter_click()
        mouse_controll.cirle_combo(rangers=6)
        self.driver.close()
        self.driver.quit() 
    
        
        
    def exit_and_saving_cookies(self):
        try:
            sleep(time_random(3))
            self.driver.close()
            self.driver.quit()
        except:
            terminal_write(text='The browser has already been disabled')
    
    
        
    def pimp_links_scanner(self, rangers=20):
        pimp_message='https://www.instagram.com/direct/t/340282366841710301244258934923015946937'
        self.driver.get(pimp_message)
        sleep(time_random(6))
        mouse_controll.scrollin(rangers=rangers, value=8)
        hrefs = self.driver.find_elements_by_tag_name('a')
        links = [item.get_attribute('href') for item in hrefs][30:]
        links=list(set(links))
        file_workers.new_folder(name='Girls')
        for link in links:
            if link not in file_workers.txt_file_update(file_path='Girls/pimp.txt'):
                file_workers.add_url(url=link,file_path='Girls/pimp.txt')
            else:
                continue
                
        
        terminal_write(text=f"pimp success {True}")
        return file_workers.txt_file_update(file_path='Girls/pimp.txt')
    
    
    
    
    
    def ignore_condidate(self,to='follow'):
        if to=='follow':
            return np.array(list(set(file_workers.txt_file_update('Followers/followers.txt'))))
        elif to=='like':
            return np.array(list(set(file_workers.txt_file_update('My_likes/likes_posts.txt'))))
        elif to=='commenting_posts':
            return np.array(list(set(file_workers.txt_file_update('Comments/commenting_posts.txt'))))
        else:
            terminal_write(text='error in ignore condidate function')
        

        
        
        

    def get_posts(self, scrolls=2):
        
        sleep(time_random(5))
        try:
            for ranger in range(scrolls):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                mouse_controll.cirle_combo(3)
            
        except Exception:
            mouse_controll.scrollin(rangers=scrolls, value=-10)
    
    
    
    
    def get_followers_links(self, links, simvol='/', my_select=4):
        links= np.array(list(set(links)))
        simvols_len=[]
        for link in links:
            simvol_get=0
            for key in link:
                if key==simvol:
                    simvol_get+=1
                else:
                    continue
            simvols_len.append(simvol_get)


        simvols_len=(np.array(simvols_len))
        true_links=(my_select==simvols_len)
        links=np.array([links[index] for index , element in enumerate(
                                        true_links) if element])    
        
        my_profile_links=DataFrame(np.array([username not in link for link in links]))[0]
        links=np.array([links[index] for index , element in enumerate(my_profile_links) if element])
        links=[link for link in links if 'facebook' not in link]
        links=[link for link in links if 'about.instagram.com' not in link]
        links=[link for link in links if 'explore' not in link]
        links=[link for link in links if 'reels' not in link]
        #reverse links
        links = links[::-1]
        return links
    
    
    
    def find_https(self, to='unfollow', scrolls=2):
        if to=='posts':
            self.get_posts(scrolls=scrolls)
            
        links=self.driver.find_elements(by=By.TAG_NAME, value='a')
        links=[link.get_attribute('href') for link in links]
        sleep(time_random(2))
        
        if to=='follow':
            return self.get_followers_links(links=links)
        
        elif to=='posts':
            links=np.array(list(set([link for link in links if "/p/" in link])))
            return links
            
        else:
            return True if np.sum(
                    [True if username in link else False for link in links]
                                    )>1 else False
    

        


            
    
    
    def all_stories_veow(self, stories=10, like_procent=0.19):
        
        self.go_website()
        stories=range(stories)
        try:
            vertical_scroll=self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div[1]/div[2]/div/div/button/div')
            mouse_controll.cirle_combo(rangers=2)
            vertical_scroll.click()
            mouse_controll.cirle_combo(rangers=1)
            vertical_scroll.click()
            vertical_scroll.click()
            mouse_controll.cirle_combo(rangers=1)
            
        except Exception as ex:
            mouse_controll.controll_click(cordinate=(851, 234), click=3, standart=1)
            mouse_controll.controll_click(cordinate=(851, 234), click=3, standart=1)

        mouse_controll.controll_click(cordinate=(762, 230), click=1)
        for story in stories:
            try:
                button_line=self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div')            
                button_line.click()
                sleep(time_random(1))
                
            except Exception:
                try:
                    key_controll.right_click()
                except Exception:
                    mouse_controll.controll_click(cordinate=(814, 621), click=1)
                    
            if np.random.random()<like_procent:
                mouse_controll.controll_click(cordinate=(710, 1023), click=1) 
            else:
                continue
            sleep(time_random(3))
        mouse_controll.controll_click(cordinate=(948, 192), click=1)
        sleep(time_random(3))
        
        
        terminal_write(text=f"story veow -> {len(stories)} success True")
        terminal_write(text=f"like_procent -> {like_procent}")
            
            
            
    

        
            
    def scanner_profile_followers(self,nickname_url_to_scan,
                                  scrolls=2,
                                  scan_by='followers'):
        self.go_profile(config=scan_by, nickname_url=nickname_url_to_scan)
            
        mouse_controll.scrollin(rangers=scrolls, value=-10)
        new_prob_nicknames=np.array(list(set([condidate for condidate in 
                    self.find_https(to='follow') if condidate not in self.ignore_condidate(to='follow')])))
                                         
        terminal_write(text=f"scan by ->{scan_by}")
        terminal_write(text=f"={len(new_prob_nicknames)} --condidate success True")
        return new_prob_nicknames
        
        
    


    
    
    def follow_one_nickname(self,nickname_url, indicator=True):
        if nickname_url not in self.ignore_condidate(to='follow'):
            self.driver.get(nickname_url)
            sleep(time_random(8))
            
            try:
                self.driver.find_element(by=By.XPATH, value="//*[text() = 'Follow']").click()
                mouse_controll.cirle_combo(rangers=2)

            except Exception:
                mouse_controll.controll_click(cordinate=(502, 209), click=1)
                key_controll.escape_click()
                key_controll.tab_click()
                key_controll.enter_click()
            
            file_workers.add_url(url=nickname_url, file_path='Followers/followers.txt')
            mouse_controll.cirle_combo(rangers=3)
            terminal_write(text=f"follow to->{nickname_url.split('/')[-2]} -> success {indicator}")
        else:
            
            terminal_write(text='You have already been subscribed ', endl=False)
            terminal_write(text=f"   to this account->{nickname_url.split('/')[-2]}")


        
    def something_went_wrong(self):
        try:
            button=self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div')
            mouse_controll.cirle_combo(rangers=3)
            terminal_write(text=f"something_went_wrong {True}")
            return True
        except:
            return False
        
        
        

    

                
                
         
                    
            
    def unfollow_one_nickname(self, nickname_url, time_sleep=10):
        
        true_followers=file_workers.txt_file_update('Followers/true_followers.txt')
        
        if nickname_url not in true_followers:
            self.go_profile(config='following',
                           nickname_url=nickname_url)
            my_people=self.find_https(to='unfollow')
            key_controll.escape_click()
            
            if my_people:
                file_workers.add_url(url=nickname_url, file_path='Followers/true_followers.txt')
                file_workers.add_url(url=nickname_url, file_path='My_likes/likes_this_nicknames.txt')
                file_workers.add_url(url=nickname_url, file_path='Comments/commenting_this_nicknames.txt')
                terminal_write(text=f"this-->{nickname_url.split('/')[-2]}->is {True}")
                
                self.go_website()
                sleep(time_random(time_sleep))
                return False

            else:
                try:
                    mouse_controll.cirle_combo(rangers=2)
                    self.driver.find_element(by=By.XPATH, value="//*[text() = 'Following']").click()
                except Exception:
                    try:
                        key_controll.tab_click(rangers=1)
                        key_controll.enter_click()
                    except Exception:    
                        mouse_controll.controll_click(cordinate=(636, 212), click=1)
                        sleep(time_random(3))


                key_controll.tab_click(rangers=5)
                key_controll.enter_click()
                terminal_write(text=f"_______________{nickname_url.split('/')[-2]}-> delete ")
                sleep(time_random(time_sleep))
                self.go_website()
                return True
        
        else:
            terminal_write(text=f"this--> {nickname_url.split('/')[-2]}->is {True}", time_sleep=0.01)
            return False
            
            
            
            
            
    def unfollow_all_bad_condidate(self, scrolls, limite, time_sleep=5):
        unfollow_quantity=0
        
        self.go_profile(config='following')
        mouse_controll.scrollin(rangers=scrolls)
        nickname_urls=self.find_https(to='follow')
        for nickname_url in nickname_urls:
            if limite:
                try:
                    if self.unfollow_one_nickname(nickname_url=nickname_url,
                                               time_sleep=time_sleep):
                        limite-=1
                        unfollow_quantity+=1
                    else:
                        continue
                except:
                    terminal_write(text=f"%%%% problem with unsubscribing nickname-->{nickname_url.split('/')[-2]}")
                    continue
            else:
                break
        
        terminal_write(text=f"scanning = {len(nickname_urls)}  accounts")
        terminal_write(text=f"unfollow = {unfollow_quantity} succuess True")
        
         
            


            
    def agent_scanner(self,nickname_url):
        self.load_cookie(path='/home/np_1961/instagram/np_1961/cookies/cookies')
        self.go_profile(config='following', nickname_url=nickname_url)
        my_people=self.find_https(to='agent')
        if not my_people:
            key_controll.escape_click()
            self.load_cookie()
        return my_people
    
    
    
    
    
    
    
    
    
    
    
        #     Like methods
    
                    


        
    def like_one_post(self, post,
                     like_button_photo=(322, 456),
                     like_button_video=(589, 667)):

        if post not in self.ignore_condidate(to='like'):
            self.driver.get(post)
            sleep(time_random(7))

            
            if self.invalid_post():
                file_workers.add_url(url=post,file_path='My_likes/likes_posts.txt')
                terminal_write(text='this post invalide !!!')
                return False
            else:
                try:
                    like=self.driver.find_element(by=By.CLASS_NAME,
                                    value="xp7jhwk").click()
                    sleep(time_random(2))
                    
                except Exception:
                    mouse_controll.cirle_combo(rangers=7)
                    mouse_controll.controll_click(cordinate=like_button_video)
                    mouse_controll.controll_click(cordinate=like_button_photo, click=2)
                    
                file_workers.add_url(url=post,file_path='My_likes/likes_posts.txt')
                terminal_write(text=f"like this post success->{post}")
                
                return True
                
        else:
            return False
            
    
    
    
    
    
        
    def likes_in_limited(self,
                     posts_urls,
                     limite,
                     time_sleep=5):  
        limite=min(limite, len(posts_urls))
        likes_success=0
        for post in posts_urls:
            sleep(time_random(time_sleep))
            try:
                if limite:
                    if self.like_one_post(post=post):
                        limite-=1
                        likes_success+=1
                    else:
                        continue
                else:
                    break
                
                
                
            except Exception:
                terminal_write(text=f"Errors in post -> {post}")
                
        terminal_write(text=f"likes {likes_success} posts success True")
        
        
    def invalid_post(self):
    
        try:
            post_finder=self.driver.find_element(by=By.XPATH,
                                                value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/span')

            
            sleep(time_random(2))

            if post_finder.text=="Sorry, this page isn't available.":
                return True

        except Exception:
            return False

        
    def like_by_tags(self,
                     tags='fish',
                     scrolls=10,
                     limite=10,
                     time_sleep=5,
                     link='https://instagram.com/explore/tags/'):
        
        self.go_website()
        self.driver.get(link+tags)
        sleep(time_random(7))

        posts_urls=self.find_https(to='posts', scrolls=scrolls)
        sleep(time_random(3))

        self.likes_in_limited(
                        posts_urls=posts_urls,
                        limite=limite ,
                        time_sleep=time_sleep)
        terminal_write(text=f"like by tags -@ {tags}-> success  True")

    
    
    

        
        
        
    def like_one_nickname(self, nickname_url, limite=4, time_sleep=4):
        
        file_workers.del_url_in_txt_file(url=nickname_url,
                            file_path='My_likes/likes_this_nicknames.txt')
        try:
            self.driver.get(nickname_url)
            sleep(time_random(10))
            posts_urls=self.find_https(to='posts', scrolls=2)
            self.likes_in_limited(posts_urls=posts_urls,
                                        limite=limite,
                                        time_sleep=time_sleep)   
            return True
        except:
            return False
            
        
    def like_true_followers(self,config ,nicknames_quantity, limite, time_sleep):
        
        while True:
            random_nickname_url=get_random_url(urls=file_workers.txt_file_update('My_likes/likes_this_nicknames.txt'))

            
            if self.like_one_nickname(nickname_url=random_nickname_url,
                                limite=limite,
                                time_sleep=time_sleep):
                nicknames_quantity-=1
                terminal_write(text=f"likes on profile {random_nickname_url.split('/')[-2]} are over->" )
                terminal_write(text='################################################################')
                
                if nicknames_quantity==0:
                    break
            else:
                terminal_write(text=f"likes on profile {random_nickname_url.split('/')[-2]} Not processing !!!->" )
                
                       
                
                
                
                
    def comment_one_post(self,post):
        self.driver.get(post)
        sleep(time_random(8))
        
        if self.invalid_post():
            terminal_write(text='post invalid !!! ')
            return False
        
        if post not in self.ignore_condidate(to='commenting_posts'):
            file_workers.add_url(url=post, file_path='Comments/commenting_posts.txt')
            try:
                self.driver.find_element(By.CLASS_NAME, value='_akhn').click()
                pyperclip.copy(get_positive_emoji()+get_positive_emoji())

                key_controll.paste_and_enter()
                sleep(time_random(4))
                
                if self.find_https(to='comments'):
                    terminal_write(text=f"{pyperclip.paste()} this is the comment that was made on this post -> {post}")
                    return True
                else:
                    terminal_write(text='post non commenting !!! ')
                    return False
            except:
                
                terminal_write(text='post lock to commenting !!!')
                return False
            
            
            
            
        else:
            terminal_write(text='post has already been commented !!!')
            return False
            
            
        
            
            
    def comments_one_nickname(self,nickname_url,  limite, time_sleep):
        file_workers.del_url_in_txt_file(url=nickname_url,
                                file_path='Comments/commenting_this_nicknames.txt')
        self.driver.get(nickname_url)
        posts=list(set([post for post in self.find_https(to='posts', scrolls=2) if post not in self.ignore_condidate(to='commenting_posts')]))
        
        limite=min(limite,len(posts))
        if limite:
            while True:
                sleep(time_random(time_sleep))
                if limite!=0:
                    random_post_url=get_random_url(urls=posts)
                    posts=[post for post in posts if post!=random_post_url]
                    if self.comment_one_post(post=random_post_url):
                        limite-=1
                    else:
                        return False
                        
                        
                else:
                    terminal_write(text=f"{nickname_url} are over !!!")
                    return True
        else:
            terminal_write(text=f"this nickname has no posts or no post for this nickname --> {username}")
            terminal_write(text=f"exit this nickname -->{nickname_url}")
            return False
                
                
                
                
    def comments_true_followers(self,config, nicknames_quantity, limite, time_sleep):
        
        try:
            random_nickname_url=get_random_url(urls=file_workers.txt_file_update('Comments/commenting_this_nicknames.txt'))
            if self.comments_one_nickname(nickname_url=random_nickname_url,
                          limite=limite, 
                          time_sleep=time_sleep):
                nicknames_quantity-=1
                
            if nicknames_quantity:
                self.comments_true_followers(    config=config,
                                                 nicknames_quantity=nicknames_quantity,
                                                 limite=limite,
                                                 time_sleep=time_sleep)
            else:
                terminal_write(text='Commenting all nicknames quantity successfully !!!')

        except:
            terminal_write(text='Comment txt file is empty !!!')
            self.go_website()
                
    
def Instapy(cookies=True):
    
    if not cookies:
        instapy=INSTAPY()
        instapy.login()
        instapy.save_cookie()
        instapy.exit_and_saving_cookies()
        raise SystemExit

    else:
        instapy=INSTAPY()
        instapy.go_website()
        instapy.load_cookie()
    return instapy
    
    
    
    
    
    



