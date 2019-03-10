#!/bin/sh
echo === run ===

echo in > /sys/class/gpio/gpio3/direction
sleep 1.25
echo out > /sys/class/gpio/gpio3/direction


sleep 1


echo in > /sys/class/gpio/gpio2/direction
sleep 1
echo out > /sys/class/gpio/gpio2/direction

