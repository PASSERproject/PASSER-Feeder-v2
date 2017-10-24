#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Run setup for proximity and dht sensors.
# Note: This must be run before the software's first use on a Pi.

mkdir -p ~/sensor_libraries/DHT
mkdir -p ~/sensor_libraries/Proximity

git clone http://github.com/adafruit/Adafruit_Python_DHT ~/sensor_libraries/DHT/
git clone http://github.com/adafruit/Adafruit_Python_VCNL40xx ~/sensor_libraries/Proximity/

cd ~/sensor_libraries/DHT
sudo python ./setup.py install
cd ../Proximity
sudo python ./setup.py install
cd ../../Feeder/source_code

curl -SLs https://apt.adafruit.com/add-pin | sudo bash
sudo apt-get install -y raspberrypi-bootloader adafruit-pitft-helper raspberrypi-kernel
sudo adafruit-pitft-helper -t 35r
