#!/bin/sh
echo === run ===

echo 1 > /sys/class/gpio/gpio2/value
echo 0 > /sys/class/gpio/gpio3/value

sleep 1.25
echo 0 > /sys/class/gpio/gpio2/value
echo 1 > /sys/class/gpio/gpio3/value

sleep 1
echo 0 > /sys/class/gpio/gpio2/value
echo 0 > /sys/class/gpio/gpio3/value

