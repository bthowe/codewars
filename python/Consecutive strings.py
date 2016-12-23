def longest_consec(strarr, k):
    if (len(strarr)==0) or (len(strarr)<k) or (k<=0):
        return ''
    lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr) - k + 1)]
    return next(l for l in lst if len(l)==len(sorted(lst, key=len)[-1]))

if __name__=="__main__":
    print longest_consec(['23523', 'awrar', 'asefa', 'a', 'asghrtserfser'], 3)
