import time, json, ssl
import paho.mqtt.client as mqtt
import random

ENDPOINT = 'a3umm0lve0a4uc-ats.iot.ap-northeast-2.amazonaws.com' # set your own aws iot thing http address
THING_NAME = 'downy_pi_final' # typing your things name

sub = 'iotdemo/topic/1' # this is subscribe channel name

start = 0;

charge = 0;

def on_connect(mqttc, obj, flags, rc):
    if rc == 0:
        print('connected!!') # if this code do well, you can see this message on your terminal
        mqttc.subscribe(sub, qos=0)

def on_message(mqttc, obj, msg): # if client publish json typs message, pi will receive message by utf-8 type
    if msg.topic == sub:
        payload = msg.payload.decode('utf-8')
        j = json.loads(payload)
        print(j['OnOff'])
       
mqtt_client = mqtt.Client(client_id=THING_NAME)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.tls_set('/home/pi/Desktop/mqtt/certificate/AmazonRootCA1.pem',certfile='/home/pi/Desktop/mqtt/certificate/cf7f956a95-certificate.pem.crt',keyfile='/home/pi/Desktop/mqtt/certificate/cf7f956a95-private.pem.key',tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None) # first arg is RootCA1 file, second arg is things crt file and third arg is private key file 
mqtt_client.connect(ENDPOINT, port=8883) # usually, port 8883 is used
mqtt_client.loop_start() #threded network loop


while True:
    time.sleep(2)
    
    test = random.randint(50,55)
    test2 = random.randint(50,57)
    #test3 = random.randint(20,80)
    #test4 = random.randint(10,100)
    
    #lat = [35, 36, 37, 38, 39]
    #lan = [127,128,129,130,131]
    
    charge = charge + 18
    print("start value is")
    print(start)

    
    payload = json.dumps({'data':charge}) # this is message you will publish
    mqtt_client.publish('pi/charge',payload, qos=1) # this is publish channel name

    