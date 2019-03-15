
<h1 align="center">
  <img src="images/argus_logo.jpg" alt="argus_logo" width="200">
  <br>A.R.G.U.S.<br>
</h1>

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

Or

```sh
curl -X POST -F username=test -F password=test http://localhost:8033/action/run
```
#### About raspbian gpio
**Need in group gpio or root run**

Default pi on gpio Group


#### About hardware

- You need a raspberry PI

- Driver:
https://detail.tmall.com/item.htm?id=527306863255&spm=a1z09.2.0.0.735a2e8dUUCZCD&_u=e1nuof5e644f

- Motor:
https://detail.tmall.com/item.htm?id=42895138394&spm=a1z09.2.0.0.67002e8d7vkqM0&_u=e1nuof5ec235

![wiring_diagram](images/wiring_diagram.jpg)

