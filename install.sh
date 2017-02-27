#!/bin/bash
cp ./autodoor /etc/init.d/ && echo "copy to autodoor";
update-rc.d autodoor defaults && echo "start run autostart";
