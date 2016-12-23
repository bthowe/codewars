def reverse_words(string):
    return ' '.join(word[::-1] for word in string.split(' '))


if __name__=="__main__":
    print reverse_words('aase  be c d')
