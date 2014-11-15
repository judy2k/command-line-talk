#!/usr/bin/env python
# -*- coding: utf-8 -*-

from progressbar import *
import time


progress = ProgressBar()
for i in progress(range(80)):
  time.sleep(0.01)

# 100% |##########################################################|


widgets = ['Loading: ', Percentage(), ' ', Bar(),
           ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=20000).start()
for i in range(20000):
    pbar.update(i)
    time.sleep(.005)
pbar.finish()

# Loading:   9% |##                   | ETA:  0:01:42 177.08  B/s
