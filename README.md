
<h1 align="center">
  <img src="images/argus_logo.jpg" alt="argus_logo" width="200">
  <br>A.R.G.U.S.<br>
</h1>

![Argus_active](https://a-wing.top/assets/img/hey_siri_open_door/argus.webp)

A.R.G.U.S.
=====

> auxiliary reliable guardian undertaking system
>
> 辅助的可靠的守护者任务系统

[![Build Status](https://travis-ci.org/JRT-FOREVER/argus.svg?branch=master)](https://travis-ci.org/JRT-FOREVER/argus)

* * *

use raspberry PI as base build wifi opendoor system

用树莓派做基础的wifi开门系统

#### For archlinux
AUR https://aur.archlinux.org/argus.git


## RUN dependence

**Need python 3.x**

```sh
apt install python3-bottle

Or

pip3 install -r requirements.txt --user
```

## install
```sh
cd argus

cp config-dist.py config.py

./argus.py
```

### deb, aur, and Makefale install
```sh
systemctl start argus.service

# autostart
systemctl enable argus.service
```

### about config
[config](config-dist.py)

## test
open your browser on localhost:8033

![Argus_login](https://a-wing.top/assets/img/hey_siri_open_door/argus_login.png)

Or

```sh
curl -X POST -F username=test -F password=test http://localhost:8033/action/run
```
#### About raspbian gpio
**Need in group gpio or root run**

Default pi on gpio Group

#### Development notes(Chinese) https://a-wing.top/diy/2019/03/15/hey_siri_open_door.html


#### About hardware

- You need a raspberry PI

- Driver:
https://detail.tmall.com/item.htm?id=527306863255

- Motor:
https://detail.tmall.com/item.htm?id=42895138394

![wiring_diagram](images/wiring_diagram.jpg)

