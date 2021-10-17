#!/bin/bash

# we check os
# we ask if python is installed
# we install python
# we install ask if we install requirements
# we install requirements
# we cd into drivermonitoring
# we run python main.py

if [[ "$OSTYPE" == "win32"* ]]; then
    echo "please install windows Subsystem for Linux"
    echo "Distributions can be installed by visiting the Microsoft Store:
https://aka.ms/wslstore"
    exit 1
else
    read -p "Do you have python installed ? [Y/N]" : python
    if [[ "$python" == "y" || "$python" == "Y" || "$python" == "Yes" || "$python" == "Yes" || "$python" == "YES"]]; then

fi

