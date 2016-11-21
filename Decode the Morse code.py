def decodeMorse(morseCode):
    words_morse = [word.split(' ') for word in morseCode.strip().split('   ')]
    return ' '.join([''.join([MORSE_CODE[letters] for letters in words]) for words in words_morse])
