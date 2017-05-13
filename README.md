# argus

use raspberry PI as base build wifi opendoor system


### A.R.G.U.S.
>auxiliary reliable guardian undertaking system
>
>辅助的可靠的守护者任务系统

***
## install

      bower install

      sudo cp argus.service /etc/systemd/system/

      systemctl start argus.service


### raspbian

    sudo apt install apache2 php5
    
    sudo apt update && apt install npm
    sudo npm install -g bower
    sudo ln -s /usr/bin/nodejs /usr/bin/node
    bower install
