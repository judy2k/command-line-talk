#!/usr/bin/env python

from ConfigParser import SafeConfigParser

from os.path import dirname, join

INSTALL_DIR = dirname(__file__)

config = SafeConfigParser()
config.read([
    join(INSTALL_DIR, 'defaults.ini'),
    'home_config.ini',
    'config.ini'
])

print config.get('server', 'host')
print config.getint('server', 'port')
print config.get('server', 'url')
