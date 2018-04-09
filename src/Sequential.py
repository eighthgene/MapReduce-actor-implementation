import sys, time

import re


class CountingWords(object):

    def __init__(self):
        self.nWords = 0

    def addWord(self):
        self.nWords += 1

    def checkWord(self, word):
        return all(64 < ord(character) < 128 for character in word)

    def getNumWords(self):
        return self.nWords


class WordCount(object):

    def __init__(self):
        self.dict = {}

    def put(self, word):
        word = word.lower()
        if word in self.dict:
            self.dict[word] += 1
        else:
            self.dict[word] = 1

    def showInfo(self):
        self.dict = sorted(self.dict.items(), key=lambda x: x[1], reverse=True)
        # d_view = [(v, k) for k, v in self.dict.iteritems()]
        with open('Z:/1/reducer2.txt', 'w') as f:
            print >> f, 'Filename:', self.dict

    def checkWord(self, word):
        return all(64 < ord(character) < 128 for character in word)

    def getNumWords(self):
        return self.dict.values()


def main():
    start_time = time.time()
    wc = WordCount()
    # cw = CountingWords()
    f = open(sys.argv[1], 'r')
    for line in f:
        for word in line.split():
            word = re.sub("[^a-zA-Z]+", "", word)
            if word != '':
                # cw.addWord()
                wc.put(word)
    print wc.showInfo()
    # print "The total number of words in this text file is:", cw.getNumWords()
    # print cw.getNumWords()
    print "Execution time:  %s seconds ---" % (time.time() - start_time)


if __name__ == "__main__":
    main()

'''
def map(l,op):
    res = []
    for i in l:
        res.append(op(i))
    return res

def reduce(l,op,acc):
    if not l:
        return acc
    return reduce(l[1:],op,op(l[0],acc))

'''
