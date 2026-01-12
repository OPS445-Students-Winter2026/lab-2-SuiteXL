#!/usr/bin/env python3

# AUTHOR: MAKSYM GRYTSYUK
# AUTHOR_ID: 165549213 / MGRYTSYUK
# DATE CREATED: 2026/01/07 5:23AM

import sys

timer = 3
count = 0

if len(sys.argv) > 1:
    timer = int(sys.argv[1])

while count < timer:
    print(timer)
    timer = timer -1
print('blast off!')
