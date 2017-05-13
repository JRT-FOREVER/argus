# argus

use raspberry PI as base build wifi opendoor system


### A.R.G.U.S.
>auxiliary reliable guardian undertaking system
>
>辅助的可靠的守护者任务系统

***

## RUN dependence
    sudo apt install apache2 php5


>defaults run path /var/www/html


## install

    cd JRT-argus

    bower install

    sudo cp argus.service /lib/systemd/system/

    systemctl enable argus.service

    systemctl start argus.service


### raspbian install bower


    sudo apt update && apt install npm
    sudo npm install -g bower
    sudo ln -s /usr/bin/nodejs /usr/bin/node
    bower install
