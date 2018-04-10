'''
Example project test unit.
'''

import unittest
import sys

from pyactor.context import set_context, create_host, sleep, shutdown

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
        self.registry.bind('Reducer', self.reducer)
        self.registry.bind('Mapper', self.mapper)
        self.stdo = sys.stdout
        self.out = Outs()
        sys.stdout = self.out

    def tearDown(self):
        # This is executed after each test. Doesn't matter if the test failed
        # or was successful.
        shutdown()
        self.out.clear()
        sys.stdout = self.stdo


if __name__ == '__main__':
    print ('## Run the tests.')
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
