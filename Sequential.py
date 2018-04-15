import re
import sys
import time


class CountingWords(object):

    def __init__(self):
        """
        constructor counting words
        """
        self.nWords = 0

    def count(self, word):
        """
        increment word by 1
        :param word: word to increment
        """
        self.nWords += 1

    def write_result(self):
        """
        save results to file
        """
        with open('Files/result_seq.txt', 'w') as f:
            print >> f, self.nWords


class WordCount(object):

    def __init__(self):
        """
        constructor word count
        """
        self.dict = {}

    def count(self, word):
        """
        add word in list by value 1 o increment value if word is in list
        :param word:
        """
        word = word.lower()
        if word in self.dict:
            self.dict[word] += 1
        else:
            self.dict[word] = 1

    def write_result(self):
        """
        save results to file
        """
        self.dict = sorted(self.dict.items(), key=lambda x: x[0], reverse=False)
        with open('Files/result_seq.txt', 'w') as f:
            print >> f, self.dict


def main():
    start_time = time.time()
    if sys.argv[2] == "1":
        count = WordCount()
    else:
        count = CountingWords()
    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        print "Error! File doesn't exist!"
    for line in f:
        for word in line.split():
            word = re.sub("[^a-zA-Z]+", "", word)
            if word != '':
                count.count(word)
    count.write_result()
    print "Execution time:  %s seconds ---" % (time.time() - start_time)


if __name__ == "__main__":
    main()
