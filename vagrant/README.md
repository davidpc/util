# Running VM with Vagrant

Vagrant ([http://www.vagrantup.com](http://www.vagrantup.com)) project to quickly and easily create a development environment with one or more Virtualbox VMs. The configuration was tested using Vagrant 1.7.2 and VirtualBox 4.3.20.

## Files

* **Vagrantfile**: This file is used by Vagrant to create the VMs. All VM configuration data is stored in a separated file (vm_list.yml)

* **vm_list.yml**: This YAML file contains a list of VM definitions and associated configuration data. It is referenced by `Vagrantfile` when Vagrant instantiates the VMs.

* **setup.sh**: This shell script is called by the Vagrant shell provisioner.

## Instructions

These instructions assume that Vagrant and Virtualbox are already installed.

1) Place the files from the `vagrant` folder into a folder on your system.

2) From a terminal window, change into the folder created in step 1) are stored and run `vagrant up` to bring up the VMs specified in `vm_list.yml` and `Vagrantfile`.

3) Once Vagrant has finished creating, booting, and provisioning the VM, log into the VM using `vagrant ssh`. Default user is `vagrant` and default password is `vagrant`.

That's it, a fresh development VM is up and running. Have fun!

To stop the VM, run `vagrant halt` in the directory where the Vagrant files are.