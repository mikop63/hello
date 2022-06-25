#! /usr/bin/env python3

import datetime
import os


def do_something():
    now = datetime.datetime.now()
    return f'Hello {now}'

def application(env, start_response):
    steart_response('200 OK', [('Content-Type', 'text/html')])
    return(do_something().encode())

if __name__ == '__main__':
    if 'REQUEST_URI' in os.environ:
        print('Content-type: text/html\n\n')
    print(do_something())
