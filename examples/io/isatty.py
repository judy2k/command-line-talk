#!/usr/bin/env python

from sys import stdin, stdout, stderr

print "Piped input:",  not stdin.isatty()
print "Piped output:", not stdout.isatty()
print "Piped error:",  not stderr.isatty()
