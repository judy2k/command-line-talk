#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys
import time


def siginfo(sig, frame):
    print "Some info"
    return True


signal.siginterrupt(signal.SIGINFO, False)
signal.signal(signal.SIGINFO, siginfo)


def main(argv=sys.argv[1:]):
    print 'start'
    while True:
        print '.',
        sys.stdout.flush()
        time.sleep(1)
    print 'finish'


if __name__ == '__main__':
    main()
