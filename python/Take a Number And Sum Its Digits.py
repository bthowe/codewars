def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function

    # sum_dig = []
    # for num in xrange(a, b+1):
    #     if num==sum([int(dig)**(ind+1) for ind, dig in enumerate(str(num))]):
    #         sum_dig.append(num)
    # return sum_dig

    return [num for num in range(a, b+1) if num==sum([float(dig)**(ind+1) for ind, dig in enumerate(str(num))])]




if __name__=="__main__":
    a = 12157692622039623570
    b = 12157692622039625620
    print sum_dig_pow(a, b)
