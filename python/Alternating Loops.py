def combine(*args):
    # args2 = list(args+tuple())
    # hi = args+tuple()
    #
    # lst = []
    # i = 0
    # while len([item for l in args2 for item in l])>0:
    #     ind = (i)%len(args2)
    #     if len(args2[ind])>0:
    #         lst.append(args2[ind].pop(0))
    #     i+=1
    # return lst

    # a = []
    # max_l = max([len(lst) for lst in args])
    # for ind in xrange(max_l):
    #     for lst in list(args):
    #         if len(lst)>ind:
    #             a.append(lst[ind])
    # return a

    max_l = max([len(lst) for lst in args])
    return [lst[ind] for ind in xrange(max_l) for lst in list(args) if len(lst)>ind]






if __name__=="__main__":
    print combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8])
