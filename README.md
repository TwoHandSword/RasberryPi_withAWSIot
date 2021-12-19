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

<br>


- [how to make your own new things](makeNewThings.md)


<br>

## **2. mqtt.fx client setting**