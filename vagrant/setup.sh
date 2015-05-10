#!/bin/bash

# Initial housekeepting
export DEBIAN_FRONTEND=noninteractive

# Update package list
sudo apt-get update

# Install CVS if not already installed
if [[ ! -e /usr/bin/cvs ]]; then
    sudo apt-get -y install cvs
fi
