#!/bin/sh

# wget  https://raw.githubusercontent.com/xmayeur/spammon/master/SpamMon.conf
echo  "remove and stop existing container"
docker rm -f HomeCtrl
echo "pull the latest version"
docker pull xmayeur/HomeCtrl
echo "run the container"
docker run --name HomeCtrl --restart always -v /root/:/conf/ -v /var/log:/var/log/ xmayeur/HomeCtrl &
sleep 16
echo "bye-bye"