import re

def decipherThis(string):
    decode_phrase = []
    for word in string.split():
        first = list(chr(int(re.findall(r'\d+', word)[0])))

        phrase = []
        if re.findall(r'\D+', word):
            phrase = list(re.findall(r'\D+', word)[0][::-1])
            phrase[1:-1] = list(re.findall(r'\D+', word)[0][1:-1])

        decode_phrase.append(''.join(first + phrase))

    return ' '.join(decode_phrase)




if __name__=="__main__":
    print decipherThis('72olle 103doo 100ya')
    # print decipherThis('82yade 115te 103o')
