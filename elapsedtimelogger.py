# coding: utf-8

import os
import sys
import time
import uuid
import logging


if sys.platform == 'win32':
    default_timer = time.clock
else:
    default_timer = time.time


def default_formatter():
    return logging.Formatter('%(elapsed_time)s %(message)s')


def default_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(default_formatter())
    return handler


class Logger(object):

    def __init__(self, handler=None, message=''):
        name = '%s_%s' % (os.path.splitext(os.path.basename(__file__))[0],
                          uuid.uuid4())
        self.log = logging.getLogger(name)
        self.log.setLevel(logging.DEBUG)
        if handler is None:
            handler = default_handler()
        self.log.addHandler(handler)
        self.message = message

    def __enter__(self):
        self.start = default_timer()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        t = default_timer()
        if exc_type:
            self.log.info(self.message, extra={'elapsed_time': None})
            return False

        self.log.info(self.message, extra={'elapsed_time': t - self.start})
