import numpy as np
def rank(a):
    for ind, num in enumerate(np.sort(list(set(a))), start=min(a)):
        print ind, num
        print a
        a = map(lambda x: ind if x==num else x, a)
        print a
    return a


if __name__=="__main__":
    print rank([2,4,5,2,5,7])
    # print rank([])
