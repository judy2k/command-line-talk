#!/usr/bin/env python

import sys
import colorama
from colorama import Fore, Back, Style

if not sys.stdout.isatty():
    colorama.init(strip=True)

print Fore.RED + 'some red text'
print Back.GREEN + 'and with a green background'
print Style.BRIGHT + 'and in bright text',
print Fore.RESET + Back.RESET + Style.RESET_ALL
print 'back to normal now'
