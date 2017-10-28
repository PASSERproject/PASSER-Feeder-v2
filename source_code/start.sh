#!/bin/bash

# John Filipowicz; Andrew Ray; Mitchell Powell
# Radford University

# Purpose: Prep for and launch all necessary processes.

# Reset the internal pi clock to the time given by the real time clock.
sudo hwclock -r

# Specify where to send the DHT data.
CSV=/media/pi/FEEDER_DATA/DHT_data.csv

# If CSV is not a file, then create the file.
if [ ! -f "$CSV" ] ; then
	echo "Temperature,Humidity,TimeStamp" >> "$CSV"
fi

# Start running periodic.py, listener.py, programed_feeding.py, and server.py in the background.
# Remove '#' and the space before it to redirect stderr & stdout to logs.
./periodic.py & #>./Logs/periodic.log
./listener.py & #>./Logs/listener.log
./programed_feeding.py &
./server.py &
