#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    print "Hello,", name, "!"

if __name__ == '__main__':
    main()
