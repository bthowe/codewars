import numpy as np
def sum_pairs(lst, sum):
    lst = np.array(lst)
    for ind, l in enumerate(lst):
        lst_sum = l + lst
        for i in xrange(len(lst_sum)):
            if lst_sum[i]==sum and i!=ind:
                return [l, lst[i]]









if __name__=="__main__":
    print sum_pairs([10, 5, 2, 3, 7, 5], 10)
