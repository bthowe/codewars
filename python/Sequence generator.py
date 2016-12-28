def sequence_gen(*args):
    args = list(args)

    while True:
        yield args[0]
        args.append(sum(args))
        args.pop(0)

if __name__=="__main__":
    fib = sequence_gen(0, 1, 1)
    for i in xrange(6):
        print fib.next()
