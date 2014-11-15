#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

import logging

LOG = logging.getLogger('logtest')

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-v', '--verbose', action='store_true')

logging.basicConfig(level=logging.WARNING,
                    format="%(msg)s")

options = arg_parser.parse_args()
if options.verbose:
    logging.getLogger().setLevel(logging.DEBUG)

LOG.debug('Running main')
LOG.info('Everything is okay')
LOG.warning('EVERYTHING HAS GONE WRONG!')
