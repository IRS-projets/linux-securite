#!/usr/bin/python

import time

now = int(time.time())
first = now-62*60
for counter in range(1,61):
    string = str(first+60*counter)+ ";1;2;3;"
    print(string)
