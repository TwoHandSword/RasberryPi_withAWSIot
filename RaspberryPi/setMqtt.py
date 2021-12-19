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
