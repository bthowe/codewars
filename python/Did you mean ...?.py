import re
from itertools import combinations, chain

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    c = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return [item for item in c if len(item)>1]


class Dictionary:
    def __init__(self,words):
        self.words=words

    def find_most_similar(self, term):
        changes = 100
        closest_word = ''

        count = 0
        for word in self.words:
            # print word, term
            if len(self.words)>len(term):
                longer = word
                shorter = term
            else:
                longer = term
                shorter = word
            letters_in = [letter for letter in shorter if letter in longer]
            # print letters_in
            # print powerset(letters_in)

            for s in powerset(letters_in):
                # print s
                regex = ''
                for let in s:
                    regex += r'[A-Za-z]*' + re.escape(let)
                regex+=r'[A-Za-z]*'
                # print regex
                # print re.search(regex, longer)
                # print len(longer, len(s))
                if re.search(regex, longer) and (len(longer) - len(s))<changes:
                    changes = len(longer) - len(s)
                    closest_word = word
        return closest_word






if __name__=="__main__":
    # words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
    # test_dict=Dictionary(words)
    # print test_dict.find_most_similar('strawbery')
    # print test_dict.find_most_similar('berry')
    # print test_dict.find_most_similar('aple')

    words = ['vkholxrvjwisrk', 'cwhyyzaorpvtnlfr', 'ggcvrtxrtnafw', 'npyrgrpbdfqhhncdi', 'jcocndjkyb', 'znystgvifufptxr', 'lnjhrzfrosinb', 'jhjyasikwyufr', 'hkldhadcxrjbmkmcdi', 'qojfrlhufr', 'fxjskybblljqr', 'xrgdgqfrldwk', 'hrwuhmtxxvmygb', 'tdvibqccxr', 'xuwahveztwoor', 'clxmqmiycvidiyr', 'cpnqknjyviusknmte', 'emvquxrvvlvwvsi', 'pxyousorusjxxbt', 'ppctybxgtleipb', 'xikoctmrhpvi', 'psaysnhfrrqgxwik', 'fgtrjakzlnaebxr', 'kqijoorfkejdcxr', 'afirbipbmkamjzw', 'ljxzjjorwgb', 'ntwmwwmicnjvhtt', 'karpscdigdvucfr', 'iqkyztorburjgiudi', 'loogviwcojxgvi', 'ajacizfrgxfumzpvi', 'tklquxrnhfiggb', 'dyhxgviphoptak', 'hwzsemiqxjwfk', 'ucxmdeudiycokfnb', 'eglanhfredaykxr', 'xffrkbdyjveb', 'mhmkakybpczjbb', 'dihhiczkdwiofpr', 'zqdrhpviqslik', 'osbednerciaai', 'nnsoamjkrzgldi', 'cfvruditwcxr', 'qifwqgdsijibor', 'hirldidcuzbyb', 'fxpvfhfrujjaifr', 'iroezmixmberfr', 'sefsknopiffajor', 'riyhpvimgaliuxr', 'pdyjrkaylryr']
    test_dict=Dictionary(words)
    print test_dict.find_most_similar('rkacypviuburk') #should equal 'zqdrhpviqslik'

rkacypviuburk
tdvibqccxr
111111  1 111
vibr
60141
# i have just been taking the difference between the letters in the longer word...but need to take the max difference across both words

rkacypviuburk
zqdrhpviqslik
9
