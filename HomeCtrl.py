import paho.mqtt.client as mqtt
# import socket
import requests
from time import sleep
import sys

HOST = '192.168.0.4'
vault_url = 'http://192.168.0.4:5000/api/ID'
uid = 'iot'
hname = 'homectrl'


def get_vault(uid):
    # url = config.get('vault', 'vault_url')
    
    r = requests.get(url=vault_url + '?uid=%s' % uid)
    id = r.json()
    r.close()
    if id['status'] == 200:
        _username = id['username']
        _password = id['password']
    else:
        _username = ''
        _password = ''
    return _username, _password


def on_message(client, userdata, message):
    topic = message.topic
    msg = str(message.payload.decode('utf-8'))
    print('Received message: ' + topic + '/' + msg)
    if topic == hname + '/getStatus':
        client.publish(hname + '/status', 'alive', qos=0, retain=False)


def on_subscribe(client, userdata, mid, qos):
    print('Subscribed: ' + str(mid))


def on_connect(client, userdata, flags, rc):
    global connect_flag
    if rc == 0:
        print("connected ok")
        connect_flag = True
        client.subscribe("/SonOff_B4/#")


def publish_msg(client, topic, msg):
    global connect_flag
    try:
        client.publish(topic, str(msg), qos=0, retain=False)
    except:
        connect_flag = False
        try:
            client.connect(HOST, port=1883)
            while not connect_flag:
                print ('+')
                sleep(1)
        
            client.publish(topic, str(msg), qos=0, retain=False)

        except:
            print('Cannot connect to mqtt broker')
            connect_flag = False
            sleep(15)


def main():
    global connect_flag
    uname, pwd = get_vault(uid)
    client = mqtt.Client('home_' + hname)
    client.username_pw_set(username=uname, password=pwd)
    
    # client.subscribe(hname + '/getStatus')
    
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_connect = on_connect
    
    client.loop_start()
    
    connect_flag = False
    
    while not connect_flag:
        try:
            client.connect(HOST, port=1883)
            print('+')
            sleep(3)
            
        except:
            print('Cannot connect to mqtt broker - retrying')
            connect_flag = False
            sys.exit(1)
      
    while True:
        # do something
        topic = '/SonOff_B4/gpio/12'
        msg = '1'
        print(1)
        publish_msg(client, topic, msg)
        sleep(5)
        topic = '/SonOff_B4/gpio/12'
        msg = '0'
        publish_msg(client, topic, msg)
        print(0)
        sleep(5)


if __name__ == '__main__':
    main()
