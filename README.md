A.R.G.U.S.
=====

> auxiliary reliable guardian undertaking system
>
> 辅助的可靠的守护者任务系统

[![Build Status](https://travis-ci.org/JRT-FOREVER/argus.svg?branch=master)](https://travis-ci.org/JRT-FOREVER/argus)

* * *

use raspberry PI as base build wifi opendoor system

## RUN dependence

**Need python 3.x**

```shell
apt install python3-bottle

Or

pip3 install -r requirements.txt --user
```

## install
```
cd argus

cp config-dist.py config.py

./argus.py
```

## test

```shell
curl -X POST -F username=test -F password=test http://localhost:8080/action/run
```
#### About raspbian gpio
**Need in group gpio or root run**

Default pi on gpio Group

