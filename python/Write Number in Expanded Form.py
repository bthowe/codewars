def expanded_form(num):
    return ' + '.join(['{0}{1}'.format(digs, '0'*ind) for ind, digs in enumerate(str(num)[::-1]) if int(digs)>0][::-1])





if __name__=="__main__":
    print expanded_form(70304)
