from itertools import count, islice
from math import sqrt
import collections

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def sum_for_list(lst):
    dic_prime_factors = collections.defaultdict(list)
    for item in lst:
        for prime_factor in [i for i in islice(count(2), abs(item)) if (isPrime(i) and item%i==0)]:
            dic_prime_factors[prime_factor].append(item)
    return_lst = [[k, sum(v)] for k, v in dic_prime_factors.iteritems()]
    return_lst.sort(key = lambda x: x[0])
    return return_lst


if __name__=="__main__":
    a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
    print sum_for_list(a)
