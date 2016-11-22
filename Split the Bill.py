import numpy as np

def split_the_bill(group_dic):
    return {k: round(v - np.mean(group_dic.values()), 2) for k, v in group_dic.iteritems()}

if __name__=="__main__":
    print split_the_bill({'A': 10, 'B': 20})
