#! /bin/bash

/usr/local/bin/k3s-uninstall.sh

docker system prune -a
docker rmi $(docker images -a -q)

sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd

sudo rm -rf docker-kubernetes-prakticna-delavnica

sudo apt update
sudo apt -y upgrade
sudo apt -y dist-upgrade

sudo apt-get purge nginx nginx-common
sudo apt-get autoremove

sudo ufw status
