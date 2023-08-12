def unfollow(instapy,activate_param):

    by,scrolls,limite,time_sleep=activate_param
    instapy.unfollow_all_bad_condidate(scrolls=scrolls,
                                       limite=limite,
                                      time_sleep=time_sleep)
    return instapy
