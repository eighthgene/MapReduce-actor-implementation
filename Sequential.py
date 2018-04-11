import re
import sys
import time


class CountingWords(object):

    def __init__(self):
        self.nWords = 0

    def addWord(self):
        self.nWords += 1

    def checkWord(self, word):
        return all(64 < ord(character) < 128 for character in word)

    def getNumWords(self):
        return self.nWords

    def abs(self):
        pass

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
        with open('result_seq.txt', 'w') as f:
            print >> f, self.dict

    def checkWord(self, word):
        return all(64 < ord(character) < 128 for character in word)

    def getNumWords(self):
        return self.dict.values()


def main():
    start_time = time.time()
    wc = WordCount()
    # cw = CountingWords()
    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        print "Error! File doesn't exist!"
    for line in f:
        for word in line.split():
            word = re.sub("[^a-zA-Z]+", "", word)
            if word != '':
                # cw.addWord()
                wc.put(word)
    wc.showInfo()
    # print "The total number of words in this text file is:", cw.getNumWords()
    # print cw.getNumWords()
    print "Execution time:  %s seconds ---" % (time.time() - start_time)


if __name__ == "__main__":
    main()
