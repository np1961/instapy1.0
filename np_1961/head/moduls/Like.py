def like_by_following(instapy , activate_param):
    config ,nicknames_quantity, limite, time_sleep=activate_param
    instapy.like_true_followers(   config=config,
                                   nicknames_quantity=nicknames_quantity,
                                   limite=limite,
                                   time_sleep=time_sleep)
    return instapy    

def like_by_tags(instapy , activate_param):
    tags ,scrolls, limite, time_sleep=activate_param
    instapy.like_by_tags(tags=tags,
                    scrolls=scrolls,
                    limite=limite,
                    time_sleep=time_sleep)

    return instapy
