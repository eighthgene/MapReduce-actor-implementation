'''
Example project test unit.
'''

import unittest
import sys

from pyactor.context import set_context, create_host, sleep, shutdown

from Timer import Timer
from MapReduce import Mapper, Reducer
from Registry import Registry


class Outs(object):
    lines = ""

    def write(self, line):
        self.lines += line

    def clear(self):
        self.lines = ""


class BasicTest(unittest.TestCase):
    def setUp(self):
        # This is executed before each test.
        set_context()
        self.h = create_host()
        self.registry = self.h.spawn('Registry', Registry)
        self.reducer = self.h.spawn('Reducer', Reducer)
        self.mapper = self.h.spawn('Mapper', Mapper)
        self.timer = self.h.spawn('Timer', Timer)
        self.registry.bind('Reducer', self.reducer)
        self.registry.bind('Mapper', self.mapper)
        self.registry.bind('Timer', self.timer)
        self.url_server = '127.0.0.1'
        self.url_file = 'http://' + self.url_server + '/pg2000.txt'

        self.stdo = sys.stdout
        self.out = Outs()
        sys.stdout = self.out

    def tearDown(self):
        # This is executed after each test. Doesn't matter if the test failed
        # or was successful.
        shutdown()
        self.out.clear()
        sys.stdout = self.stdo

    def test_map(self):
        # This is the test. You can put as much of them as you want. The name
        # must begin with 'test'.
        self.mapper.start_map(self.url_file, self.reducer, self.timer)

    def test_unbind(self):
        self.registry.unbind('Reducer')
        self.registry.unbind('Mapper')
        self.registry.unbind('Timer')
        self.assertEqual(self.registry.lookup('mapper'), None)
        self.assertListEqual(self.registry.get_all(), [])

    def test_timer(self):
        self.out.clear()
        self.timer.initial_time()
        sleep(1)
        self.timer.final_time()
        self.assertEqual(self.timer.final_time, 'Execution time:  1.000s seconds ---"')


if __name__ == '__main__':
    print ('## Run the tests.')
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
