def tickets(people):
    cash_register = {100:0, 50:0, 25:0}

    for bill in people:
        cash_register[bill]+=1

        if bill==100:
            cash_register[50]+=-1
            cash_register[25]+=-1

            cash_register[25]+=-3

        elif bill==50:
            cash_register[25]+=-1


if __name__=="__main__":
    tickets([25, 25, 50])
