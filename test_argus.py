import unittest

#import argus
from argus import *
import os

class TestFrequency(unittest.TestCase):
    def test_limit(self):
        f = Frequency()
        self.assertEqual(f.limit('aaa'), False)

        list(map(lambda x: f.limit(x), ['aaa', 'aaa', 'bbb', 'aaa', 'aaa']))
        #for x in ['aaa', 'aaa', 'bbb', 'aaa', 'aaa']:
        #  f.limit(x)

        self.assertEqual(len(f.cache), 4)
        self.assertEqual(f.limit('aaa'), True)

    def test_clear(self):
        f = Frequency()
        list(map(lambda x: f.limit(x), ['aaa', 'aaa', 'bbb', 'aaa', 'aaa']))
        f.clear('aaa')
        self.assertEqual(len(f.cache), 1)

    def test_clean(self):
        f = Frequency()
        list(map(lambda x: f.limit(x), ['aaa', 'aaa', 'bbb', 'aaa', 'aaa']))
        f.clean()
        self.assertEqual(len(f.cache), 0)
        #print(f.cache)

class TestExecutor(unittest.TestCase):
    def test_init(self):
        actions = {
          'init_action': 'echo -n init_action > init_action',
          'before_action': 'echo -n before_action > before_action',
          'exec_action': 'echo -n exec_action > exec_action',
          'after_action': 'echo -n after_action > after_action',
          'del_action': 'echo -n del_action > del_action'}

        e = Executor(actions)
        e.execute('exec_action')

        for a in actions.keys():
            #print(a)
            #a = 'init_action'
            with open(a, 'r') as f:
                self.assertEqual(f.read(), a)
            os.remove(a)


class TestChecker(unittest.TestCase):
    users = [
        {'user': 'test_pass_text', 'pass_text': '233'},
        {'user': 'test_pass_text_2', 'pass_text': '233'},

        # password == '233'
        {'user': 'sha1', 'pass_sha1': '52fdb9f68c503e11d168fe52035901864c0a4861'},
        {'user': 'sha1s', 'pass_sha1': '52fdb9f68c503e11d168fe52035901864c0a4861'},

        # password == '233'
        {'user': 'salt_sha1', 'pass_salt+sha1': '55f68+ccda65a9e8964ea6977a27d79228608aa1e80a4a'},
        {'user': 'test', 'pass_text': '233'}
    ]
    def test_check(self):
        pass

    def test_pass_text(self):
        c = Checker(self.users)

        # True
        s, a = c.check('test_pass_text_2', '233')
        self.assertEqual(s, True)
        self.assertTrue(isinstance(a, dict))

        # No user match
        s, a = c.check('test_pass_textii', '233')
        self.assertEqual(s, False)
        self.assertTrue(isinstance(a, dict))
        self.assertEqual(len(a), 0)

        # Password error
        s, a = c.check('test_pass_text', '233333')
        self.assertEqual(s, False)
        self.assertTrue(isinstance(a, dict))

    def test_pass_sha1(self):
        c = Checker(self.users)

        # True
        s, a = c.check('sha1', '233')
        self.assertEqual(s, True)
        self.assertTrue(isinstance(a, dict))


    def test_pass_saltsha1(self):
        c = Checker(self.users)

        # True
        s, a = c.check('salt_sha1', '233')
        self.assertEqual(s, True)
        self.assertTrue(isinstance(a, dict))

if __name__ == '__main__':
    unittest.main()

