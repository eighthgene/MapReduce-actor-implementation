import urllib2


class Mapper(object):
    _ask = []
    _tell = ['start_map']
    _ref = ['start_map']

    reducer = None
    data = None
    actor = None
    timer = None

    def map(self, data):
        """
        Definition of map method
        :param data: String data chank of text
        :return: dictionary: key, value.
        """
        pass

    def start_map(self, url_file_chank, ref_reducer, timer_actor):
        """
        Call this method from the main to to initialization and start map function
        :param url_file_chank: URL of chunks file
        :param ref_reducer: Reference to reducer actor
        :param timer_actor: Reference to timer actor
        """
        self.data = urllib2.urlopen(url_file_chank)
        self.timer = timer_actor
        self.timer.start_timer()
        self.reducer = ref_reducer
        result_mapper = self.map(self.data)
        self.reducer.obtain_map_results(result_mapper)


class Reducer(object):
    _ask = ['get_status']
    _tell = ['obtain_map_results', 'set_parameters']

    num_mappers = None
    num_mappers_finished = 0
    file_handler = None
    file_path = None
    output_filename = None
    timer = None

    result_dict = []

    def obtain_map_results(self, map_results):
        """
        Method for obtain partial result from one mapper and start timer if is the first call of function
        :param map_results: dictionary, result of mapper
        """
        self.num_mappers_finished += 1
        self.result_dict.append(map_results)
        if self.num_mappers_finished >= self.num_mappers:
            self.start_reducer()

    def start_reducer(self):
        """
        Method for start reducing all results of mappers saved in result_dict
        """
        reduce_result = self.reduce(self.result_dict)
        self.timer.stop_timer()
        if reduce_result is not None:
            self.save_to_file(reduce_result)
        self.file_handler.clear()
        print 5 * '#' + ' Reducer finished ' + 5 * '#'

    def set_parameters(self, num_maps, file_handler, file_path, output_filename, timer_actor):
        """
        Setter of reducer
        :param num_maps: number of mapper in system
        :param file_handler: object of FileHandler
        :param file_path: path of file
        :param output_filename: name of file for save results
        :param timer_actor: timer actor
        """
        self.num_mappers = num_maps
        self.file_handler = file_handler
        self.file_path = file_path
        self.output_filename = output_filename
        self.timer = timer_actor

    def save_to_file(self, result):
        """
        Save results of reducer in file, sorted by key alphabetically
        :param result: save dictionary to file
        """
        with open(self.file_path + '/' + self.output_filename, 'w') as f:
            print >> f, sorted(result.items(), key=lambda x: x[0], reverse=False)

    def reduce(self, data):
        """
        Definition of reduce method
        :param data: list of dictionaries to reduce
        :return: dictionary of data reduced
        """
        return self.result_dict
