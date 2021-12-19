# **3. make mqtt setting script and run on RaspberryPi**

<br>

```bash
$ curl https://bootstrap.pypa.io/get-pip.py | sudo python3
```
- you should install pip and python3 on your Pi

<br>

```bash
$ sudo python3 -m pip install paho-mqtt
```
- and then install paho-mqtt, this is a package for mqtt in python

<br>


```python
import time, json, ssl
import paho.mqtt.client as mqtt
import random

ENDPOINT = '' # set your own aws iot thing http address
THING_NAME = '' # typing your things name

sub = '' # this is subscribe channel name

def on_connect(mqttc, obj, flags, rc):
    if rc == 0:
        print('connected!!') # if this code do well, you can see this message on your terminal
        mqttc.subscribe(sub, qos=0)

def on_message(mqttc, obj, msg): # if client publish json typs message, pi will receive message by utf-8 type
    if msg.topic == sub:
        payload = msg.payload.decode('utf-8')
        j = json.loads(payload)
        print(j['message'])

mqtt_client = mqtt.Client(client_id=THING_NAME)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.tls_set('',certfile='',keyfile='',tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None) # first arg is RootCA1 file, second arg is things crt file and third arg is private key file 
mqtt_client.connect(ENDPOINT, port=8883) # usually, port 8883 is used
mqtt_client.loop_start() #threded network loop

while True:
    time.sleep(2)
    test = random.randint(0,180)

    payload = json.dumps({'action':test}) # this is message you will publish
    mqtt_client.publish('',payload, qos=1) # this is publish channel name

```

- above smaple code is make one publish channel and one subscribe channel. if you want to run this script, you should fill some empty properties like channel name, certifiacte path on Pi and etc.

![aws-iot17](https://user-images.githubusercontent.com/41497254/146681491-17a97040-481c-486d-a3dd-60ffe4023fca.png)

- then run this script, you can see "connected!!" message

![aws-iot18](https://user-images.githubusercontent.com/41497254/146681520-e4155696-45ec-4b23-85b3-0dbf6518c635.png)


- then you can see mqtt message from Pi on your PC [Pi -> PC]

![aws-iot19](https://user-images.githubusercontent.com/41497254/146681548-b57eaa8b-b852-41e5-828a-a6d6cf84f821.png)


- also you can publish jSON message from PC, and then Pi can recieve jSON message by utf-8 decoding