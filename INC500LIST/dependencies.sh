#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y build-essential checkinstall wget tar
sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo apt-get install -y docker.io

wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xzf Python-3.6.2.tgz
cd Python-3.6.2
./configure
sudo make altinstall

sudo pip3.6 -V
sudo pip3.6 install -r requirment.txt

echo Congratulations! All Dependencies had been successfully installed ^vv^

