class VigenereAutokeyCipher():
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, phrase):
        KeyPhrase = self.key_phrase(phrase)
        encoded = ''
        for i in xrange(len(phrase)):
            if phrase[i] in self.alphabet:
                encoded+=self.alphabett(KeyPhrase[i], phrase[i])
            else:
                encoded+=phrase[i]
        return encoded

    def key_phrase(self, phrase):
        key_list = [letter for letter in self.key]
        phrase_list = [letter for letter in phrase if letter in self.alphabet]
        KeyPhrase = ''
        for letter in phrase:
            if letter in self.alphabet:
                if key_list:
                    KeyPhrase+=key_list.pop(0)
                else:
                    let = phrase_list.pop(0)
                    KeyPhrase+=let
                    phrase_list.append(let)
            else:
                KeyPhrase+=letter
        return KeyPhrase

    def decode(self, phrase):
        key_list = [letter for letter in self.key]

        decoded = ''
        for letter in phrase:
            if letter in self.alphabet:
                decoded_letter=self.alphabett(key_list.pop(0), letter, encode=False)
                decoded+=decoded_letter
                key_list.append(decoded_letter)
            else:
                decoded+=letter
        return decoded

    def alphabett(self, key_letter, letter, encode=True):
        # print key_letter, letter
        if letter not in self.alphabet:
            return letter
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

    # print c.encode("it's a shift cipher!")
    # print c.decode("xt'k s ovzib vapzlz!")
