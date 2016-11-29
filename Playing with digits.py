def dig_pow(n, p):
    p_sum = sum([int(num)**(p + ind) for ind, num in enumerate(str(n))])
    k = p_sum/n
    print k
    if k*n==p_sum:
        return k
    else:
        return -1

if __name__=="__main__":
    print dig_pow(46288, 5)
