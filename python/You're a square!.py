def is_square(n):
    # if n<0:
    #     return False
    # return n**.5 - int(n**.5)==0

    return (n>=0) and (n**.5 - int(n**.5)==0)


if __name__=="__main__":
    print is_square(-1)
