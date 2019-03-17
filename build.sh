#!/bin/sh

git pull
docker rm -f homectrl

sudo chmod +x *.sh
sudo cp HomeCtrl.sh HomeCtrl.conf /root

docker build -t homectrl .
docker tag homectrl xmayeur/homectrl
docker push xmayeur/homectrl

# docker run -ti --name homectrl --dns 8.8.8.8 -v /root/:/conf/ -v /var/log:/var/log/ homectrl


