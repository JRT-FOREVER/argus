#!/bin/bash
echo "deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ wheezy main non-free contrib
deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ wheezy main non-free contrib" > /etc/apt/sources.list && echo "update sources to ustc"
