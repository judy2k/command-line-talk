#!/usr/bin/env python

import click

@click.group()
def main():
    pass

@main.command()
@click.option('--to', default='world')
def greet(to):
    print "Hello,", to, "!"

@main.command()
@click.option('--to', default='world')
def ungreet(to):
    print "Goodbye,", to, "!"

if __name__ == '__main__':
    main()
