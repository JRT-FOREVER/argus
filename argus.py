#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, logging
from bottle import get, post, run, template, request, redirect, static_file

from lib.argus import Executor, Frequency, Checker

import config


ex = Executor(config.actions)
user = Checker(config.users)
f = Frequency()


@get('/')
def index():
    return template('lib/argus', name='argus', target='/action/' + config.default_action)

@get('/assets/<filename>')
def server_static(filename):
    return static_file(filename, root='public')

#@post('/login') # or @route('/login', method='POST')
@post('/action/<action>')
def do_login(action):
    ip = request.get('REMOTE_ADDR')
    if not f.limit(ip):
        status, u = user.check(request.forms.get('username'), request.forms.get('password'))

        if status:
            f.clear(ip)
            ex.run(action)
            redirect("/")
        else:
            return "<p>Login failed.</p>"

    else:
        ex.execute('alarm_action')
        return "<p>Login failed.</p>"

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s -- : %(message)s')
    logging.info('=== Start ' + config.name + ' ===')
    logging.debug('This message should go to the log file')
    #run(host=config.host, port=config.port, reloader=True)
    run(host=config.host, port=config.port)

    # Need gunicorn
    #run(host=config.host, port=config.port, server='gunicorn', workers=1)

