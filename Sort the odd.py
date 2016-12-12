def sort_array(source_array):
    sorted_odds = sorted([num for num in source_array if num%2==1])

    # lst = []
    # for num in source_array:
    #     if num%2==0:
    #         lst.append(num)
    #     else:
    #         lst.append(sorted_odds.pop(0))
    # return lst

    return  [num if num%2==0 else sorted_odds.pop(0) for num in source_array]


if __name__=="__main__":
    print sort_array([5, 3, 2, 8, 1, 4])
    print sort_array([5, 3, 1, 8, 0])
    print sort_array([])
