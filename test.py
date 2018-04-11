'''
Example project test unit.
'''

import unittest
import sys

import time
from pyactor.context import set_context, create_host, sleep, shutdown

from Timer import Timer
from MapReduce import Mapper, Reducer
from Registry import Registry
from WordCount import MapImpl


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

    def test_unbind(self):
        self.assertEqual(self.registry.lookup('Timer'), self.timer)
        self.registry.unbind('Reducer')
        self.registry.unbind('Mapper')
        self.registry.unbind('Timer')
        self.assertEqual(self.registry.lookup('mapper'), None)
        self.assertListEqual(self.registry.get_all(), [])

    def test_timer(self):
        self.out.clear()
        self.timer.initial_time = time.clock()
        sleep(1)
        self.timer.final_time = time.clock() - self.timer.initial_time
        self.assertIsNot(self.timer.final_time, 0)

    def test_map(self):
        data = open('./Files/pg2000.txt', 'r')
        mapper = MapImpl()
        result = mapper.map(data)
        dict_distributed = eval(open('./Files/result_distributed.txt').read())
        result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        self.assertEqual(len(result), len(dict_distributed))


if __name__ == '__main__':
    print ('## Run the tests.')
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
