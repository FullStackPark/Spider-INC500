#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y build-essential checkinstall wget tar
sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo apt-get remove docker docker-engine docker.io

sudo apt-get install -y \
    linux-image-extra-$(uname -r) \
    linux-image-extra-virtual

sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install -y docker-ce

apt-cache madison docker-ce

sudo apt-get install -y --allow-downgrades docker-ce=17.06.0~ce-0~ubuntu

wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xzf Python-3.6.2.tgz
cd Python-3.6.2
./configure
sudo make altinstall

sudo pip3.6 -V
sudo pip3.6 install -r requirment.txt

sudo rm -rf Python-3.6.2 
sudo rm -rf Python-3.6.2.tgz

echo Congratulations! All Dependencies had been successfully installed ^vv^

