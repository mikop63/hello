#! /usr/bin/env python3

import datetime


def do_something():
    now = datetime.datetime.now()
    return f'Hello {now}'

if __name__ == '__main__':
    print(do_something())
