def mango(quantity, price):
    num = 0
    while quantity>0:
        if quantity>=3:
            quantity += -3
            num += 2
        else:
            num += quantity
            quantity = 0
    return num*price





if __name__=="__main__":
    print mango(9, 5)
