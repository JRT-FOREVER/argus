#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from bottle import route, run, template, request
import sys, logging

from lib.argus import Executor, Frequency, Checker

import config

print(config.name)

ex = Executor(config.actions)
user = Checker(config.users)
f = Frequency()


@route('/')
def index():
    return template('argus', name='argus', target='/action/' + config.default_action)

@route('/token/<name>')
def index(name):
    return check_token(name)

@route('/login/<user>/<passwd>')
def index(user, passwd):
    return executor()

#@post('/login') # or @route('/login', method='POST')
@route('/action/<action>', method='POST')
def do_login(action):
    ip = request.get('REMOTE_ADDR')
    if not f.limit(ip):
        status, u = user.check(request.forms.get('username'), request.forms.get('password'))

        if status:
            f.clear(ip)
            ex.run(action)
            return "<p>Your login information was correct.</p>"
        else:
            return "<p>Login failed.</p>"

    else:
        ex.execute('alarm_action')
        return "<p>Login failed.</p>"

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s -- : %(message)s')
    logging.info('=== Start ' + config.name + ' ===')
    logging.debug('This message should go to the log file')
    #run(host='localhost', port=8080, reloader=True)
    run(host='0.0.0.0', port=8080)

