def my_crib(n):
    house = ''
    for ind in xrange(n):
        house += '{0}/{1}\\{2}\n'.format(' '*(n-ind) , ' '*2*ind, ' '*(n-ind))
    house += '/{0}\\\n'.format('_'*2*n)
    for ind in xrange(n-1):
        house += '|{0}|\n'.format(' '*2*n)
    house += '|{0}|'.format('_'*2*n)
    return house





if __name__=="__main__":
    print my_crib(1)
