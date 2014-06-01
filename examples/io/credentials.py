#!/usr/bin/env python

import getpass

username = getpass.getuser()
password = getpass.getpass()

print "You are", username, \
    "and you should never use the password '", password, \
    "' again!"
