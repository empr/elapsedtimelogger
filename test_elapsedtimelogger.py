# coding: utf-8

import re
import logging
import unittest
from StringIO import StringIO

from elapsedtimelogger import Logger, default_formatter


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.buffer = StringIO()
        self.handler = logging.StreamHandler(self.buffer)

    def _getvalue(self):
        return self.buffer.getvalue()

    def _loop(self, num=10000):
        for i in range(num):
            pass

    def test_basic(self):
        self.handler.setFormatter(default_formatter())
        with Logger(handler=self.handler):
            self._loop()

        value = float(self._getvalue().strip())
        self.assertTrue(value > 0)

    def test_message(self):
        self.handler.setFormatter(default_formatter())
        with Logger(handler=self.handler, message='test'):
            self._loop()

        buf = self._getvalue().strip().split(' ')
        self.assertTrue(float(buf[0]) > 0)
        self.assertEqual(buf[1], 'test')

    def test_message_by_instance(self):
        self.handler.setFormatter(default_formatter())
        with Logger(handler=self.handler) as log:
            log.message = 'test'

        value = self.buffer.getvalue().strip()
        buf = self._getvalue().strip().split(' ')
        self.assertTrue(float(buf[0]) > 0)
        self.assertEqual(buf[1], 'test')

    def test_raise_in_with_statement(self):
        self.handler.setFormatter(default_formatter())
        try:
            with Logger(handler=self.handler):
                1 / 0
        except:
            pass

        value = self._getvalue().strip()
        self.assertEqual(value, 'None')

    def test_custom_formatter(self):
        fmt = logging.Formatter('%(asctime)s %(elapsed_time)s %(message)s')
        self.handler.setFormatter(fmt)
        with Logger(handler=self.handler) as log:
            log.message = 'test'

        buf = self._getvalue().strip().split(' ')
        self.assertTrue(re.match(r'\d{4}-\d{2}-\d{2}', buf[0]))
        self.assertTrue(re.match(r'\d{2}:\d{2}:\d{2},\d+', buf[1]))
        self.assertTrue(float(buf[2] > 0))
        self.assertEqual(buf[3], 'test')

    def test_multi_with_statement(self):
        self.handler.setFormatter(default_formatter())
        with Logger(handler=self.handler):
            self._loop()

        with Logger(handler=self.handler):
            self._loop()

        values = [x.strip() for x in self._getvalue().split('\n') if x]
        self.assertEqual(len(values), 2)


if __name__ == '__main__':
    unittest.main()
