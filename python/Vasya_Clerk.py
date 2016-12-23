def tickets(people):
    path = [(people, {100:0, 50:0, 25:0})]
    final_cash = []

    while path:
        p = path.pop(0)
        # print p

        line = p[0]
        bill = line.pop(0)
        # print line
        cash_register = p[1]
        cash_register[bill]+=1

        if bill==100:
            cash_register_new = cash_register.copy()

            cash_register[50]+=-1
            cash_register[25]+=-1
            if line:
                path.append((list(line), cash_register.copy()))
            else:
                final_cash.append(cash_register.copy())

            cash_register_new[25]+=-3
            if line:
                path.append((list(line), cash_register_new))
            else:
                final_cash.append(cash_register_new.copy())

        elif bill==50:
            cash_register[25]+=-1
            if line:
                path.append((list(line), cash_register.copy()))
            else:
                final_cash.append(cash_register.copy())
        else:
            if line:
                path.append((list(line), cash_register.copy()))
            else:
                final_cash.append(cash_register.copy())
        # print p

        # print path
    # print final_cash
    for p in final_cash:
        if len([val for val in p.values() if val<0])==0:
            return 'YES'
    return 'NO'



if __name__=="__main__":
    print tickets([25, 25, 25, 50, 100, 25, 50])
