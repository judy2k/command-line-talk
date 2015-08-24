#!/usr/bin/env python
# -*- coding: utf-8 -*-

from progressbar import ProgressBar
import click
import time


with click.progressbar(range(80)) as numbers:
    for i in numbers:
        time.sleep(0.01)


with click.progressbar(length=20000) as pbar:
    for i in range(20000):
        pbar.update(1)
        time.sleep(.0005)
