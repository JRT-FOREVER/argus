#!/bin/sh
echo === init ===

echo 2 > /sys/class/gpio/export
echo 3 > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio2/direction
echo out > /sys/class/gpio/gpio3/direction

