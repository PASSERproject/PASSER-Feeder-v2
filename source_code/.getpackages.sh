#!/bin/bash

# John Filipowicz, Mitchell Powell
# Radford University

# Purpose: This script is meant to download/install all packages needed for the feeder to operate

# Packages will be installed by sections



# Update System
sudo apt-get update

# Upgrade System
sudo apt-get upgrade

# Sensors
sudo apt-get install build-essential python-dev

# Webcam
sudo apt-get install streamer imagemagick libav-tools libav-doc

# Genetic Algorithm
sudo apt-get install libapache2-mod-php5 php5 php-pear apache2 apache2-utils
sudo apt-get install php5-xcache php5-mysql php5-curl php5-gd

# Python Imaging Library and TKinter
sudo apt-get install python-imaging
sudo apt-get install python-imaging-tk
sudo apt-get install python3-pil.imagetk
