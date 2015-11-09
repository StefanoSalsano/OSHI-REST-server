# OSHI REST Server

## Introduction

Server for common OSHI REST endpoints

## Setup
You can use the OSHI-REST-server.sh script to setup and run this project.

The available options are:
- --mode (or -m) to choose the running mode: setup, run

1. Download the VirtualBox VM from [Uniroma2 Netgroup](http://netgroup.uniroma2.it/twiki/bin/view/Oshi/WebHome#AnchorSoftDown)
2. After starting the VM, run the following command as user `user`:
    ```
    cd /home/user/workspace
    
    git clone https://github.com/netgroup/OSHI-REST-server.git
    ```
3. Setup the environment:
    ```
    cd /home/user/workspace/OSHI-REST-server
    
    sudo ./OSHI-REST-server.sh --mode setup
    ```
## Run instructions

1. Run the server:
    ```
    cd /home/user/workspace/OSHI-REST-server
    
    ./OSHI-REST-server.sh --mode run
    ```