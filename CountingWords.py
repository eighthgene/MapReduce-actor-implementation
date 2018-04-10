
import re
from collections import Counter

from Master import Master
from MapReduce import Mapper, Reducer


class MapCountingWords(Mapper):
    def map(self):
        results = {}
        for line in self.data:
            line_words = line.split()
            for word in line_words:
                word = re.sub("[^a-zA-Z]+", "", word)
                if word in results:
                    results['appearences'] += 1
                else:
                    results['appearences'] = 1
        return results


class ReduceCountingsWords(Reducer):

    def reduce(self, list_of_dict):
        reduced_dict = {}
        for dictionary in list_of_dict:
            tmp_dict = dict(dictionary)
            reduced_dict = dict(Counter(tmp_dict) + Counter(reduced_dict))
        return reduced_dict


class WordCount(Master):
    pass


if __name__ == '__main__':
    # Parameters
    # ip host (Master)
    # Url HTTP Server
    # Input file path
    # Output path
    # Name output file (.txt)
    mapReduce = WordCount('192.168.0.22',
                          '192.168.0.22:8000',
                          'Z:/1/pg2000.txt', 'Z:/1/', 'res.txt',
                          'CountingWords/MapCountingWords', 'CountingWords/ReduceCountingsWords')
    mapReduce.run()

