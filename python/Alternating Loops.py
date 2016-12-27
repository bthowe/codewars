def combine(*args):
    args = list(args)

    lst = []
    i = 0
    while len([item for l in args for item in l])>0:
        ind = (i)%len(args)
        if len(args[ind])>0:
            lst.append(args[ind].pop(0))
        i+=1
    return lst








if __name__=="__main__":
    combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8])
