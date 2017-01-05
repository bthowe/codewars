from string import ascii_lowercase
def decrypt(test_key):
    return ''.join([str(test_key.count(c)) for c in ascii_lowercase])


# another technique is using ord('a') which will give the ascii value for 'a', chr(ord('a')) will give it back






if __name__=="__main__":
    print decrypt('$aaaa#bbb*ccfff!z')
