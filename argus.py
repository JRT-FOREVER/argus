#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from bottle import route, run, template
import sys, logging

import config

print(config.name)

import os
class Executor():
    def __init__(self, actions=config.actions):
        self.actions = actions
        self.__exec(self.actions['init_action']) if 'init_action' in self.actions else None

    def execute(self, action):
        self.__exec(self.actions['before_action']) if 'before_action' in self.actions else None
        tmp = self.__exec(self.actions[action])
        self.__exec(self.actions['after_action']) if 'after_action' in self.actions else None
        return tmp

    def __exec(self, cmd):
        return os.system(cmd)

    def __del__(self):
        self.__exec(self.actions['del_action']) if 'del_action' in self.actions else None

class Frequency():
    def __init__(self, fail=3, mix_cache=10):
        self.fail = fail
        self.mix_cache = mix_cache
        self.cache = []

    def limit(self, ip=''):
        true = True if self.cache.count(ip) >= self.fail else self.cache.append(ip)
        self.cache.pop(0) if len(self.cache) >= self.mix_cache else None
        return True if true else False

    def clear(self, ip):
        self.cache = list(filter(lambda x: x != ip, self.cache))

    def clean(self):
        return self.cache.clear()


import hashlib
class Checker():
    def __init__(self, users):
        self.users = users

    def check(self, username, password):
        users = list(filter(lambda x: x['user'] == username, self.users))
        if len(users) >= 1:
            # Get only the first data
            user = users[0]
            encryptions = ['pass_text', 'pass_sha1', 'pass_salt+sha1']
            # Get only the first data
            e = list(filter(lambda x: x in user, encryptions))[0]
            if e == 'pass_text':
                status = True if user[e] == password else False
            elif e == 'pass_sha1':
                status = True if user[e] == hashlib.sha1(password.encode()).hexdigest() else False
            elif e == 'pass_salt+sha1':
                salt, sha1 = user[e].split('+', 1)
                status = True if sha1 == hashlib.sha1((salt + password).encode()).hexdigest() else False
            else:
                raise

            return status, user

        else:
            return False, {}


@route('/')
def index():
		return template('argus', name='argus', target='/hello/2333333')
    #return '<b>Hello llllllllllllllll</b>!'

@route('/token/<name>')
def index(name):
    return check_token(name)

@route('/login/<user>/<passwd>')
def index(user, passwd):
    return executor()

#@post('/login') # or @route('/login', method='POST')
#def do_login():
#    username = request.forms.get('username')
#    password = request.forms.get('password')
#    if check_login(username, password):
#        return "<p>Your login information was correct.</p>"
#    else:
#        return "<p>Login failed.</p>"

#@route('/my_ip')
#def show_ip():
#    ip = request.environ.get('REMOTE_ADDR')
#    # or ip = request.get('REMOTE_ADDR')
#    # or ip = request['REMOTE_ADDR']
#    return template("Your IP is: {{ip}}", ip=ip)

#check_token('23333')
#check_token("9f3d9739b11c2a4b08ea48512ac467f6")

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(levelname)s -- : %(message)s')
    logging.info('=== Start ' + config.name + ' ===')
    logging.debug('This message should go to the log file')
    #run(host='localhost', port=8080, reloader=True)

