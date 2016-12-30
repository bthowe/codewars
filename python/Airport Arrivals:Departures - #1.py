def flap_display(lines, rotors):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'

    new_lines = []
    for i, word in enumerate(lines):
        new_word = []
        while rotors[i]:
            turns = rotors[i].pop(0)
            turned_letters = [alpha[(alpha.index(letter) + turns)%len(alpha)] for letter in word]
            new_word.append(turned_letters.pop(0))
            word = ''.join(turned_letters)
        new_lines.append(''.join(new_word))
    return new_lines






if __name__=="__main__":
    before = ['RAT', 'CAT', 'PEE']
    rotors = [[2, 5, 32], [1, 13, 27], [2, 48, 13]]
    print flap_display(before, rotors)
