import numpy as np
import re
def decodeBits(bits):
    bits = bits.strip('0')
    if '0' in bits.strip('0'):
        
        letters = re.findall(r'([1]+)\1*', bits)
        word_unit = np.min([len(let) for let in letters])

        gaps = re.findall(r'([0]+)\1*', bits)
        gap_unit = np.min([len(gap) for gap in gaps])

        time = np.min([word_unit, gap_unit])

        items = [('-', '1'*time*3), ('   ', '0'*time*7), (' ', '0'*time*3), ('.', '1'*time), ('', '0'*time)]
        for item in items:
            # print item[0], item[1]
            bits = bits.replace(item[1], item[0])

        return bits
    else:
        bits = bits.strip('0')

        letters = re.findall(r'([1]+)\1*', bits)
        time = np.min([len(let) for let in letters])

        items = [('-', '1'*time*3), ('   ', '0'*time*7), (' ', '0'*time*3), ('.', '1'*time), ('', '0'*time)]
        for item in items:
            # print item[0], item[1]
            bits = bits.replace(item[1], item[0])

        return bits

def decodeMorse(morseCode):
    words_morse = [word.split(' ') for word in morseCode.strip().split('   ')]
    return ' '.join([''.join([MORSE_CODE[letters] for letters in words]) for words in words_morse])


if __name__=="__main__":
    # print decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
    # print decodeBits('1110111')
    print decodeBits('1')
