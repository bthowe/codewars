def anagrams(word, words):
    return [w for w in words if ''.join(sorted(w))==''.join(sorted(word))]




if __name__=="__main__":
    # print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
    # print anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
    print anagrams('laser', ['lazing', 'lazy',  'lacer'])
