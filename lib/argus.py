
import os
class Executor():
    def __init__(self, actions=[]):
        self.actions = actions
        self.execute('init_action')

    def run(self, action):
        self.execute('before_action')
        tmp = self.execute(action)
        self.execute('after_action')
        return tmp

    def execute(self, action):
        return self.__exec(self.actions[action]) if action in self.actions else False

    def __exec(self, cmd):
        return os.system(cmd)

    def __del__(self):
        self.execute('del_action')

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



