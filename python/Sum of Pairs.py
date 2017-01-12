import numpy as np

def sum_pairs(lst, sum):
    # nums = []
    # index_sum = 10**10
    # for ind1, addend1 in enumerate(lst[:-1]):
    #     for ind2, addend2 in enumerate(lst[ind1+1:]):
    #         if addend1 + addend2 == sum:
    #             if ind1+ind2+1<index_sum:
    #                 index_sum = ind1+ind2+1
    #                 nums = [addend1, addend2]
    # if nums:
    #     return nums
    # return None


# perhaps a faster way...still times out
    add_mat = np.array([lst]).T + np.array([lst]*len(lst))

    add_triu = np.triu(add_mat, 1) - sum*np.tri(len(lst))

    mask = np.where(add_triu==sum)
    if len(mask[0])>0:
        index = min(zip(mask[0], mask[1]), key = lambda x: max(x))

        return [lst[index[0]], lst[index[1]]]
    return None









if __name__=="__main__":
    print sum_pairs([1, 4, 8, 7, 3, 15], 8)
