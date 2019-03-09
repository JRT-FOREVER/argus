name = "argus"
#action = "./argus.sh"
actions = ''
# aciton:
# init_action
# before_action
# after_action
# del_action

# alarm_action

tokens = [
  # echo 233 | md5sum
  "9f3d9739b11c2a4b08ea48512ac467f6",
  # echo 456 | md5sum
  "d2d362cdc6579390f1c0617d74a7913d"
]

users = [
  { 'user': 'admin', 'pass_text': 'admin'},
  # echo -n <You Password> | sha1sum
  # tmp_str=`head /dev/urandom | md5sum | head -c 5`; echo ${tmp_str}+`echo -n ${tmp_str}<You Password> | sha1sum`
  { 'user': 'test', 'pass_text': 'admin'}
]

