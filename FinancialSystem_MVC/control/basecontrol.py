#!/usr/bin/python
# -*- coding: <encoding name> -*-

from logger import logger

class BaseControl(object):

    def __init__(self, args={}, session={}):
        self.args = args
        self.session = session

        logger.info('args --{}'.format(self.args))

