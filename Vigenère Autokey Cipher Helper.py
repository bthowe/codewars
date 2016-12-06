class VigenereAutokeyCipher():

# check whether letter is in alphabet

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
        key_phrase_list = [letter for letter in self.key]
        phrase_list = [letter for letter in phrase.replace(' ', '')]

        decoded = ''
        for i in xrange(len(phrase)):
            if phrase[i]!=' ':
                decoded_letter=self.alphabett(key_phrase_list.pop(0), phrase_list.pop(0), encode=False)
                decoded+=decoded_letter
                key_phrase_list.append(decoded_letter)
            else:
                decoded+=' '
        return decoded

    def key_phrase(self, phrase):
        word_iter = (self.key + phrase).replace(' ', '')
        list_phrase = [letter for letter in phrase]
        index = 0
        for ind in xrange(len(list_phrase)):
            if list_phrase[ind]!=' ':
                list_phrase[ind]=word_iter[index%len(word_iter)]
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

    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # key = 'password'
    # c = VigenereAutokeyCipher(key, alphabet)

    # print c.encode('amazingly few discotheques provide jukeboxes') # returns 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'
    # print c.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib') # returns 'amazingly few discotheques provide jukeboxes'
    # print c.encode('codewars'); # returns 'rovwsoiv'
    # print c.decode('laxxhsj'); # returns 'waffles'

    print c.encode('AAAAAAAAPASSWORDAAAAAAAA') # returns 'rovwsoiv'
    print c.decode('PASSWORDPASSWORDPASSWORD') # returns 'waffles'
