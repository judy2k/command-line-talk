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
    " Print A_LIST_OF_WORDS with a space in-between. "
    for word in A_LIST_OF_WORDS:
        print word, len(word)


def two(argv):
    " Print A_LIST_OF_WORDS in fixed-width columns. "
    for word in A_LIST_OF_WORDS:
        print "{word:15}  {length:>2}".format(
            word=word,
            length=len(word))


def three(argv):
    """
    PrintA_LIST_OF_WORDS with the first column width generated from the
    longest item.
    """
    max_width = max(len(w) for w in A_LIST_OF_WORDS)
    for word in A_LIST_OF_WORDS:
        print "{word:{col_width}} {length:>2}".format(
            word=word, length=len(word), col_width=max_width)


def four(argv):
    """
    Print A_LIST_OF_WORDS as rows of tabular data with
    appropriately-sized columns.
    """
    format_table([(word, word, len(word)) for word in A_LIST_OF_WORDS])


def format_table(rows):
    """
    Print a
    """
    cols = zip(*rows)
    widths = [max(len(str(w)) for w in col) for col in cols]
    for row in rows:
        for i, val in enumerate(row):
            print "{0:{1}}".format(val, widths[i]),
        print


def main(argv=sys.argv[1:]):
    action = globals()[next(iter(argv), 'one')]
    action(argv[1:])


if __name__ == '__main__':
    main()
