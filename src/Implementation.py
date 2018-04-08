import collections
import urllib2

import re


class Mapper(object):
    _ask = []
    _tell = ['start_map']
    _ref = ['start_map']

    reducer = None
    data = None

    def map(self):
        results = []
        for line in self.data:
            line_words = line.split()
            for word in line_words:
                word = re.sub("[^a-zA-Z]+", "", word)
                if word != '':
                    # lowercase words
                    results.append((word.lower(), 1))
        return results

    # def map(self):
    #     results = []
    #     for line in self.data:
    #         line_words = line.split()
    #         for word in line_words:
    #             if self.is_valid_word(word):
    #                 # lowercase words
    #                 results.append(('', 1))
    #     return results

    # def is_valid_word(self, word):
    #     return all(64 < ord(character) < 128 for character in word)

    def start_map(self, url_file_chank, ref_reducer):
        self.data = urllib2.urlopen(url_file_chank)
        self.reducer = ref_reducer
        result_mapper = self.map()
        self.reducer.obtain_map_results(result_mapper)


class Reducer(object):
    _ask = ['get_status']
    _tell = ['obtain_map_results', 'set_parameters']

    num_mappers = None
    num_mappers_finished = 0
    file_handler = None
    file_path = None
    output_filename = None
    status = False

    results = collections.defaultdict(list)

    def obtain_map_results(self, map_results):
        self.num_mappers_finished += 1
        map(lambda w: self.results[w[0]].append(w[1]), map_results)
        if self.num_mappers_finished >= self.num_mappers:
            self.start_reducer()

    def start_reducer(self):
        result = self.reduce(self.results)
        self.status = True
        self.save_to_file(result)
        self.file_handler.clear()
        print 5 * '#' + ' Reducer finished ' + 5 * '#'

    def set_parameters(self, num_maps, file_handler, file_path, output_filename):
        self.num_mappers = num_maps
        self.file_handler = file_handler
        self.file_path = file_path
        self.output_filename = output_filename

    def save_to_file(self, result):
        d_view = [(v, k) for k, v in result.iteritems()]
        d_view.sort(reverse=True)  # natively sort by first element
        with open(self.file_path + self.output_filename, 'w') as f:
            print >> f, 'Filename:', [["%s: %d" % (k, v)] for v, k in d_view]

    def reduce(self, data):
        results = {}
        for res in data.items():
            results[res[0]] = sum(res[1])
        return results

    def get_status(self):
        return self.status
