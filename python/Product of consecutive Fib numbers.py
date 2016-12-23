# fibonacci sequence generator
def fibo():
    x0 = 0
    yield x0

    x1 = 1
    yield x1

    x2 = x0 + x1

    go = 1
    while go==1:
        yield x2
        x0 = x1
        x1 = x2
        x2 = x0 + x1


### my submission
# def productFib(prod):
#     x0 = 0
#     x1 = 1
#     x2 = x0 + x1
#
#     while x0*x1<prod:
#         x0 = x1
#         x1 = x2
#         x2 = x0 + x1
#
#     if x0*x1==prod:
#         return [x0, x1, True]
#     else:
#         return [x0, x1, False]


### a cooler answer
def productFib(prod):
    a, b = 0, 1
    while a*b < prod:
        a, b = b, a + b
    return [a, b, a*b == prod]

if __name__=="__main__":
    print productFib(4895)
