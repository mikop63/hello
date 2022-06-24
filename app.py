#! /usr/bin/env python3

import datetime
import os


def do_something():
    now = datetime.datetime.now()
    return f'Hello {now}'

if __name__ == '__main__':
    if 'REQUEST_URI' in os.environ:
        print('Content-type: text/html\n\n')
    print(do_something())
