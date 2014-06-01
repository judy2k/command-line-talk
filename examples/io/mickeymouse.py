#!/usr/bin/env python

import sys

# Print to stdout:
print "You've seen this all before."

# Print to stderr:
print >>sys.stderr, "This is not *standard* output"

# Read from stdin:
for line in sys.stdin:
    print line,
