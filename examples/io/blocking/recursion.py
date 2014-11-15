#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys


def g(word):
    if len(word) < 2:
        return [word]
    else:
        first, rest = word[0], word[1:]
        results = []
        options = g(rest)
        for item in options:
            for i in range(len(item)+1):

                results.append(item[:i] + first + item[i:])
        return options + results


def main(argv=sys.argv[1:]):
    arg_parser = argparse.ArgumentParser()

    options = arg_parser.parse_args(argv)
    print sorted(g('abcd'))


if __name__ == '__main__':
    main()
