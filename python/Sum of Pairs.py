# import numpy as np
# def sum_pairs(lst, sum):
#     index_sum = -1
#     nums = []
#     for ind, l in enumerate(lst[:-1]):
#         lst_sum = l + np.array(lst[ind+1:])
#         print lst_sum
#         index = np.where(lst_sum[::-1]==sum)[0]
#         if len(index)>0:
#             if index_sum<int(index):
#                 index_sum = int(index)
#                 nums = [l, lst[-(index_sum+1)]]
#     if nums:
#         return nums
#     return None

def sum_pairs(lst, sum):
    nums = []
    index_sum = 10**10
    for ind1, addend1 in enumerate(lst[:-1]):
        for ind2, addend2 in enumerate(lst[ind1:]):
            if addend1 + addend2 == sum:
                if ind1+ind2+1<index_sum:
                    index_sum = ind1+ind2+1
                    nums = [addend1, addend2]
    if nums:
        return nums
    return None


if __name__=="__main__":
    print sum_pairs([10, 5, 1, 0, 2, 7, 2, 9], 7)
