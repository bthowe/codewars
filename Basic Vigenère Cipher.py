class VigenereAutokeyCipher():

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, phrase):
        kp = self.key_phrase(phrase)
        encoded = ''
        for i in xrange(len(phrase)):
            if phrase[i]!=' ':
                encoded+=self.alphabett(kp[i], phrase[i])
            else:
                encoded+=' '
        return encoded

    def decode(self, phrase):
        kp = self.key_phrase(phrase)
        decoded = ''
        for i in xrange(len(phrase)):
            if phrase[i]!=' ':
                decoded+=self.alphabett(kp[i], phrase[i], encode=False)
            else:
                decoded+=' '
        return decoded

    def key_phrase(self, phrase):
        list_phrase = [letter for letter in phrase]
        index = 0
        for ind in xrange(len(list_phrase)):
            if list_phrase[ind]!=' ':
                list_phrase[ind]=self.key[index%len(self.key)]
                index+=1
        return ''.join(list_phrase)

    def alphabett(self, key_letter, letter, encode=True):
        if encode:
            index = self.alphabet.index(key_letter)
            new_alphabet = self.alphabet[index:] + self.alphabet[:index]

            letter_index = self.alphabet.index(letter)
            return new_alphabet[letter_index]
        else:
            index = self.alphabet.index(key_letter)
            new_alphabet = self.alphabet[index:] + self.alphabet[:index]

            letter_index = new_alphabet.index(letter)
            return self.alphabet[letter_index]


if __name__=="__main__":
    key = 'PASSWORD'
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c = VigenereAutokeyCipher(key, abc)

    print c.encode('AAAAAAAAPASSWORDAAAAAAAA') # returns 'rovwsoiv'
    print c.decode('PASSWORDPASSWORDPASSWORD') # returns 'waffles'
