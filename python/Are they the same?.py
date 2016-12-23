import numpy as np
def comp(array1, array2):
    if array1==None or array2==None:
        return False
    else:
        return False not in [i[0]**2==i[1] for i in zip(np.sort(array1), np.sort(array2))]



if __name__=="__main__":
    # a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    # a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    a1 = []
    a2 = []
    print comp(a1, a2)
