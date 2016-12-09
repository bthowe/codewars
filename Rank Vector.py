import numpy as np
def rank(a):
    ranky = 1
    b = a
    for num in np.sort(list(set(a)))[::-1]: #or reversed(np.sort(list(set(a))))
        count = np.sum(np.where(np.array(a)==num, 1, 0))
        b = map(lambda x: '{}'.format(ranky) if x==num else x, b)
        ranky+=count
    return map(int, b)






if __name__=="__main__":
    print rank([2,4,5,2,5,7])
    # print rank([1,2,2,2,3,3])
    # print rank([])
