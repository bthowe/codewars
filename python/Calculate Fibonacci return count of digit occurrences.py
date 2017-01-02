from collections import Counter

def fib(n):
    n0 = 0
    n1 = 1

    count = 1
    while count<n:
        n2 = n0 + n1
        n0 = n1
        n1 = n2
        count+=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n2

def fib_digits(n):
    fib_num = fib(n)

    return sorted([(v, int(k)) for k, v in dict(Counter(str(fib_num))).iteritems()])[::-1]

    # print Counter(str(fib_num)).items()




if __name__=="__main__":
    print fib_digits(100000)
