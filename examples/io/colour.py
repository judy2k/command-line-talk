#!/usr/bin/env python

from colorama import Fore, Back, Style
print Fore.RED + 'some red text'
print Back.GREEN + 'and with a green background'
print Style.BRIGHT + 'and in bright text',
print Fore.RESET + Back.RESET + Style.RESET_ALL
print 'back to normal now'
