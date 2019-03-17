#!/bin/sh

git pull
docker rm -f HomeCtrl

# sed -i "s/debug = True/debug = False/g" SpamMon.conf

sudo chmod +x *.sh
sudo cp HomeCtrl.sh HomeCtrl.conf /root

docker build -t HomeCtrl .
docker tag HomeCtrl xmayeur/HomeCtrl
docker push xmayeur/HomeCtrl

# docker run -ti --name HomeCtrl --dns 8.8.8.8 -v /root/:/conf/ -v /var/log:/var/log/ HomeCtrl


