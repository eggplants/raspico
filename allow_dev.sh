#!/bin/bash

sudo usermod -a -G dialout "$(whoami)"
if [ -z "$1" ]
then
  sudo chmod a+rw /dev/ttyACM0
else
  sudo chmod a+rw "$1"
fi
