def dbl_linear(n):
    seq = [1]
    i = 0
    while i<n:
        x = seq[i]
        seq.append(2*x + 1)
        seq.append(3*x + 1)
        seq = list(set(seq))
        seq.sort()
        i+=1
    return seq[n]



if __name__=="__main__":
    print dbl_linear(20)
