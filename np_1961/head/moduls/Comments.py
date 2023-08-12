def comments(instapy, activate_param):
    config,nicknames_quantity,limite,time_sleep=activate_param
    instapy.comments_true_followers(config=config,
                               nicknames_quantity=nicknames_quantity,
                               limite=limite,
                               time_sleep=time_sleep)
    return instapy
