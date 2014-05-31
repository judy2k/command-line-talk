#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

A_LIST_OF_WORDS = ['installation',
                   'Chamicuro',
                   'foliiferous',
                   'spermatic',
                   'intemperately',
                   'pederastically',
                   'proctosigmoidectomy',
                   'begar']


def one(argv):
    for word in A_LIST_OF_WORDS:
        print word, len(word)


def two(argv):
    max_width = max(len(w) for w in A_LIST_OF_WORDS)
    for word in A_LIST_OF_WORDS:
        print "{word:{col_width}} {length}".format(
            word=word,
            align='<',
            col_width=max_width,
            length=len(word))


def main(argv=sys.argv[1:]):
    action = globals()[next(iter(argv), 'one')]
    action(argv[1:])


if __name__ == '__main__':
    main()
