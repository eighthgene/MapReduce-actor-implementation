import time
from pyactor.context import set_context, create_host, serve_forever
from FileHandler import FileHandler


class Master(object):

    def __init__(self, ip, url_server,
                 input_file_path, output_dir, output_filename,
                 map_implementation, reduce_implementation):
        # Ip
        self.ip = ip
        self.url_server = url_server

        # File path
        self.input_file_path = input_file_path
        self.output_dir = output_dir
        self.output_filename = output_filename

        # Map and reduce classes implementation
        self.map_impl = map_implementation
        self.reduce_impl = reduce_implementation

    def run(self):
        url_file = 'http://' + self.url_server + '/'
        ip = self.ip

        set_context()
        host = create_host('http://' + str(ip) + ':6002')

        registry = host.lookup_url('http://' + str(ip) + ':6000/regis', 'Registry',
                                   'Registry')

        list_workers = registry.get_all_names()
        print 'Workers registered in server: ' + str(list_workers)

        num_workers = len(list_workers)
        print 'Number of workers: ' + str(num_workers)

        print 'Start file splitter...'
        file_handler = FileHandler(self.input_file_path, self.output_dir)
        file_handler.split_file(num_workers)
        print 'Finish splitting...'

        # Create Timer Actor
        if not host.has_actor('timer'):
            timer = host.spawn('timer', 'Timer/Timer')
        else:
            timer = host.lookup('timer')

        # Create reducer
        if not host.has_actor('reducer'):
            reducer = host.spawn('reducer', self.reduce_impl)
        else:
            reducer = host.lookup('reducer')
        reducer.set_parameters(num_workers, file_handler, self.output_dir, self.output_filename, timer)

        #timer.start_timer()

        # Create mapper actors
        for i in range(num_workers):
            remote_host = registry.lookup(list_workers[i])
            # print remote_host
            if remote_host is not None:
                if not remote_host.has_actor('mapper'):
                    worker = remote_host.spawn('mapper', self.map_impl)
                else:
                    worker = remote_host.lookup('mapper')
                print "Mapper created in host -> " + list_workers[i]

                url_file_chank = url_file + "file_" + str(i) + '.txt'
                worker.start_map(url_file_chank, reducer, timer)

        # Unbind Workers
        # print "Start unbinding Workers."
        # for i in range(num_workers):
        #     registry.unbind(list_workers[i])

        serve_forever()
