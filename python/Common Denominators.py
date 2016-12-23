from fractions import gcd
# import numpy as np
import itertools

def lcm(n1, n2):
    return (n1*n2)/gcd(n1, n2)

def lcm_list(lst):
    return list(set([lcm(pair[0], pair[1]) for pair in itertools.combinations(lst, 2)]))

def convertFracts(lst):
# too slow
    # denoms = np.array(map(lambda x: x[1], lst))
    #
    # prod = np.max(denoms)
    # factor = 2
    # while not all(np.where(prod%denoms==0, True, False)):
    #     prod = factor*np.max(denoms)
    #     factor+=1
    # return [[l[0]*prod/l[1], prod] for l in lst]


    lyst = map(lambda x: x[1], lst)
    while len(lyst)>1:
        lyst = lcm_list(lyst)
    l_c_m = lyst[0]
    return [[l[0]*l_c_m/l[1], l_c_m] for l in lst]




if __name__=="__main__":
    a = [[1, 2], [1, 3], [1, 4]]
    b = [[6, 12], [4, 12], [3, 12]]
    print convertFracts(a)
    print convertFracts(a)==b
