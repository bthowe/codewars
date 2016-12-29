import numpy as np
def sum_pairs(lst, sum):
    index_sum = -1
    nums = []
    for ind, l in enumerate(lst[:-1]):
        lst_sum = l + np.array(lst[ind+1:])
        index = np.where(lst_sum[::-1]==sum)[0]
        if len(index)>0:
            if index_sum<int(index):
                index_sum = int(index)
                nums = [l, lst[-(index_sum+1)]]
    if nums:
        return nums
    return None

if __name__=="__main__":
    print sum_pairs([10, 5, 2, 3, 7, 5, 0], 7)
