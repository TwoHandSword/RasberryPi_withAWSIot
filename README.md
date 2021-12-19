# **RasberryPi with AWS IOT**

#### using AWS IOT, build "mqtt" communtion between Host PC and Pi

<br>
<br>
<br>

## **pre-work**

1. Download latest Rasbian on your own Pi. <https://www.raspberrypi.com/software/operating-systems/> <br> 
    1-1. [**Recommend**] When accessing your own pie, use the VNC Viewer. <br>
    1-2. [**Recommend**] After setting up wifi with your router, connect to pi via putty terminal on host pc. After that, by hitting the command below, an ip address that can be accessed by Vnc viewer is generated.
    ```bash
    vnc server -geometry 1920x1080
    ```
    **-geometry** option is Resolution adjustment options.

2. Sign up for aws. [because we use aws IOT service]
3. Download mqtt.fx [**freeversion**] <https://www.jensd.de/wordpress/?p=2746>

<br>
<br>
<br>

## **How to build mqtt communication**

<br>

## **1. make new Things**

![aws-iot1](https://user-images.githubusercontent.com/41497254/146670679-cb9715f0-408c-46e1-a19d-8ed5502dc82d.png)

- push "Create things"

![aws-iot2](https://user-images.githubusercontent.com/41497254/146670793-75f893fe-78b1-4f39-af1b-eff5f41288d1.png)

- Create single thing

![aws-iot3](https://user-images.githubusercontent.com/41497254/146670810-853c1361-6872-4c27-85a4-b73f57922b1f.png)

- please type name what you want 

![aws-iot4](https://user-images.githubusercontent.com/41497254/146670824-693500fe-2b9a-4ace-bff3-13a74edcac57.png)

- if you want, you can make auto-generated a new certificate 

![aws-iot5](https://user-images.githubusercontent.com/41497254/146670926-79711236-c7de-4161-96e3-cc23fc916efd.png)

- now you have your onw things

<br>

## **2. mqtt.fx client setting**