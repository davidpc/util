#!/bin/bash

# Initial housekeepting
export DEBIAN_FRONTEND=noninteractive

# Update package list
sudo apt-get update
sudo apt-get install linux-headers-generic build-essential dkms -y

# Install CVS if not already installed
if [[ ! -e /usr/bin/cvs ]]; then
    sudo apt-get -y install cvs &> /dev/null
fi

sudo useradd -m -p $(openssl passwd -1 "mininet") mininet
