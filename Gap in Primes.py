from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def gap(gap, start, stop):
    primes_list = []
    i = start
    while i<stop+1:
        if isPrime(i):
            primes_list.append(i)
            if i - primes_list[0]==gap:
                return primes_list
            else:
                if len(primes_list)!=1:
                    del primes_list[0]
        i+=1
    return None


if __name__=="__main__":
    print gap(6,100,110)
