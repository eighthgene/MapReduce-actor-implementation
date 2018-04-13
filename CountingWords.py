import re
from collections import Counter

from Master import Master
from MapReduce import Mapper, Reducer


class MapCountingWords(Mapper):

    @classmethod
    def map(cls, data):
        counter = 0
        results = {}
        for line in data:
            line_words = line.split()
            for word in line_words:
                word = re.sub("[^a-zA-Z]+", "", word)
                if word != '':
                    counter += 1
        results['Total words'] = counter
        return results


class ReduceCountingsWords(Reducer):

    @classmethod
    def reduce(cls, list_of_dict):
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
    mapReduce = WordCount('10.110.173.52',
                          '10.110.173.52:8000',
                          './Files/Sample.txt', './Files', 'result_distributed.txt',
                          'CountingWords/MapCountingWords', 'CountingWords/ReduceCountingsWords')
    mapReduce.run()
