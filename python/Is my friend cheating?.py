import itertools

def removNb(n):
    seq = range(1, n+1)
    seq_sum = sum(seq)

    #### this took too long to run
    # return [tup for tup in itertools.permutations(seq, 2) if tup[0]*tup[1]==(seq_sum - tup[0] - tup[1])]

    #### still too slow
    # lst = [tup for tup in itertools.combinations(seq, 2) if tup[0]*tup[1]==(seq_sum - tup[0] - tup[1])]
    # final_lst = []
    # for tup in lst:
    #     final_lst.append(tup)
    #     final_lst.append((tup[1], tup[0]))
    # return sorted(final_lst, key=lambda x: x[0])

    



if __name__=="__main__":
    print removNb(26)
