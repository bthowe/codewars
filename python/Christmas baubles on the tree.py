def baubles_on_tree(baubles, branches):
    if branches==0:
        return "Grandma, we will have to buy a Christmas tree first!"
    a, b = divmod(baubles, branches)
    branch = [a]*branches

    ind = 0
    while b>0:
        branch[ind]+=1
        b+=-1
        ind+=1
    return branch

    # return [a+1] * b + [a] * (branches - b) would have been more clever








if __name__=="__main__":
    print baubles_on_tree(11,5)
