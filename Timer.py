import time


class Timer(object):
    _ask = ['']
    _tell = ['start_timer', 'stop_timer']
    _ref = ['']

    initial_time = None
    final_time = None

    def start_timer(self):
        """
        save time of start program
        """
        if self.initial_time is None:
            self.initial_time = time.time()
            print "Timer started!"
        else:
            pass

    def stop_timer(self):
        """
        calculate running time program and print results
        """
        self.final_time = time.time()
        print "Execution time:  %s seconds ---" % (self.final_time - self.initial_time)
