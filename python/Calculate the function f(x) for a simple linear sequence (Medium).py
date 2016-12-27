def get_function(sequence):
    m = (sequence[-1] - sequence[0])/4.
    b = sequence[0]
    fun = lambda x: b + m*x

    if all([fun(i)==sequence[i] for i in xrange(len(sequence))]):
        return fun
    return 'Non-linear sequence'




if __name__=="__main__":
    print get_function([0, 3, 6, 9, 12])(10)
