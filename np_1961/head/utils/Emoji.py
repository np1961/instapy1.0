import emoji
from random import randint

def get_menu_emoji():
    emojize_name=[':busts_in_silhouette:',':skull:', ':love_letter:',':growing_heart:',':movie_camera:',':left_speech_bubble:']
    emojize=[emoji.emojize(name) for name in emojize_name]
    return emojize

def get_positive_emoji():
    emojies_comments_names=[':slightly_smiling_face:',':waving_hand:',':thumbs_up:',':collision:',':hundred_points:']
    emojies_by_comments=[emoji.emojize(emoji_name) for emoji_name in emojies_comments_names] 
    random_index=randint(0,len(emojies_by_comments)-1)
    return emojies_by_comments[random_index]
    
    
