import re
from collections import Counter

from Master import Master
from MapReduce import Mapper, Reducer


class MapImpl(Mapper):

    @classmethod
    def map(cls, data):
        """
        Map method
        :param data: String data chank of text
        :return: dictionary: key, value.
        """
        results = {}
        for line in data:
            line_words = line.split()
            for word in line_words:
                word = re.sub("[^a-zA-Z]+", "", word)
                if word != '':
                    word = word.lower()
                    # lowercase words
                    # results.append((word.lower(), 1))
                    if word in results:
                        results[word] += 1
                    else:
                        results[word] = 1
        return results


class ReduceImpl(Reducer):

    @classmethod
    def reduce(cls, list_of_dict):
        """
        Reduce method
        :param list_of_dict: list of dictionaries
        :return: dictionaries reduced
        """
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
    mapReduce = WordCount('10.110.173.35',
                          '10.110.173.35:8000',
                          './Files/Sample.txt', './Files', 'result_distributed.txt',
                          'WordCount/MapImpl', 'WordCount/ReduceImpl')
    mapReduce.run()
