import numpy as np

def rot_90_clock(strng):
    s = np.array([[letter for letter in line] for line in strng.split('\n')])
    return '\n'.join([''.join([str(number) for number in row]) for row in np.rot90(s, 3)])

def diag_1_sym(strng):
    s = np.array([[letter for letter in line] for line in strng.split('\n')])
    return '\n'.join([''.join([str(number) for number in row]) for row in np.fliplr(np.rot90(s, 3))])

def selfie_and_diag1(strng):
    return '\n'.join(["{0}|{1}".format(a, b) for a, b in zip(strng.split('\n'), diag_1_sym(strng).split('\n'))])

def oper(fct, s):
    return fct(s)






if __name__=="__main__":
    strng = "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb"
    # print np.array([[letter for letter in line] for line in strng.split('\n')])
    # print oper(rot_90_clock, strng)
    # print oper(diag_1_sym, strng)
    print oper(selfie_and_diag1, strng)

    # strng ="abcd\nefgh\nijkl\nmnop"
    # print np.array([[letter for letter in line] for line in strng.split('\n')])
    # strng ="aeim\nbfjn\ncgko\ndhlp"
    # print np.array([[letter for letter in line] for line in strng.split('\n')])
