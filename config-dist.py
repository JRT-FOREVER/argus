name = "argus"
default_action = 'test_exec'

# hook aciton:
#     init_action : App start run
#     before_action : Action run before run
#     after_action : Action run after run
#     del_action : App stop run

# alarm_action : Run this aciton. not run before_action && after_action

actions = {
    # 'init_action': 'echo -n init_action > init_action',
    # 'before_action': 'echo -n before_action > before_action',
    'test_exec': 'echo ++++++++++++++++++++++++++',
    # 'after_action': 'echo -n after_action > after_action',
    # 'del_action': 'echo -n del_action > del_action',
    'alarm_action': 'echo AAAAAAAAAAAAAAAAAAAAA'}


users = [
  { 'user': 'admin', 'pass_text': 'admin'},
  # echo -n <You Password> | sha1sum
  # tmp_str=`head /dev/urandom | md5sum | head -c 5`; echo ${tmp_str}+`echo -n ${tmp_str}<You Password> | sha1sum`
  { 'user': 'test', 'pass_text': 'admin'}
]

