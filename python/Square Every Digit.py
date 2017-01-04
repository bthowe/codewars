def square_digits(num):
    return int(''.join([str(int(dig)**2) for dig in str(num)]))

if __name__=="__main__":
    print square_digits(9119)
