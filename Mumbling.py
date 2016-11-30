def accum(s):
    # my submission
    # return '-'.join([(letter.lower()*(ind+1)).title() for ind, letter in enumerate(s)])

    # the lower() method is unnecessary. also, instead of ind+1 I can just say enumerate(s, 1)
    return '-'.join([(letter*ind).title() for ind, letter in enumerate(s, 1)])



if __name__=="__main__":
    print accum("ZpglnRxqenU")
