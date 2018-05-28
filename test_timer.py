# -*- coding: utf-8 -*-

import gevent

def test(a, b):
    print a,b

loop = gevent.get_hub().loop
t = loop.timer(0.0, 5)

timer.start(test, 1, 2)
loop.run()

