name = 'argus'
#default_action = 'test_exec'
default_action = 'run'

# hook aciton:
#     init_action : App start run
#     before_action : Action run before run
#     after_action : Action run after run
#     del_action : App stop run

# If someone violently cracks your password
# alarm_action : Run this aciton. not run before_action && after_action

actions = {
    # 'init_action': 'echo -n init_action > init_action',
    'init_action': 'sh scripts/init.sh',
    # 'before_action': 'echo -n before_action > before_action',
    #'test_exec': 'echo ++++++++++++++++++++++++++',
    'run': 'sh scripts/run.sh',
    # 'after_action': 'echo -n after_action > after_action',
    # 'del_action': 'echo -n del_action > del_action',
    'del_action': 'sh scripts/del.sh',
    'alarm_action': 'echo AAAAAAAAAAAAAAAAAAAAA'}


# Priority queue : pass_text > pass_sha1 > pass_salt+sha1

users = [
    # password == 'admin'
    #{'user': 'admin', 'pass_text': 'admin'},

    # password == '233'
    # echo -n <You Password> | sha1sum
    #{'user': 'sha1', 'pass_sha1': '52fdb9f68c503e11d168fe52035901864c0a4861'},

    # password == 'admin'
    #{'user': 'pass_233', 'pass_text': 'admin', 'pass_sha1': '52fdb9f68c503e11d168fe52035901864c0a4861'},

    # password == '233'
    # tmp_str=`head /dev/urandom | md5sum | head -c 5`; echo ${tmp_str}+`echo -n ${tmp_str}<You Password> | sha1sum`
    #{'user': 'salt_sha1', 'pass_salt+sha1': '55f68+ccda65a9e8964ea6977a27d79228608aa1e80a4a'},

    {'user': 'test', 'pass_text': 'test'}
]

