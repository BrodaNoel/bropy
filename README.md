# BroPy
BroPy, a full suite for RaspberryPi control.
Each project has its own folder and documentation.

Sorry for my english. Feel free to send Pull Request fixing my languaje mistakes.

## You have to know, before starting
* The RaspberryPi used for this project, is `RaspberryPi 2 Model B` (https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)
* Your RaspberryPi should use `NOOBS` (https://www.raspberrypi.org/downloads/noobs/).
* We recommend restart your RaspberryPi SO before follow the guide (read mor about it in next steps)
* Your RaspberryPi is using the user by default (user: pi, password: raspberry)
* Your PC/Mac should has installed some software to access to the RaspberryPi by SSH (We recommend PuTTY for Windows, and SSH command is pre installed in Mac)
* You will need a display connected to the RaspberryPi using HDMI and a KeyBoard connected by USB.
* We recommend to have a USB-WiFi device, just in case.

## Restart RaspberryPi SO
We recommend to reset your RaspberryPi before starting.
In case you want to do it, read all these steps, and then follow them one by one:

* Connect the keyboard and display at the RaspberryPi
* Power on the RaspberryPi.
* Hold pressed SHIFT key to start in recovery mode.
* Press `i` to reinstall Raspbian. You will see a warning, press `Yes` (enter).
* Go for a coffee. This process takes too long (~15 minutes).
* After installation, you will get another message. press `Ok` (enter).

Your RapsberryPi is ready to be used. Let's do the magic.

## Configure keyboard
* Press `Windows` key to open the Menu.
* Open `Preferences > Mouse and Keyboard Settings`
* Good luck!

## Configure WiFi to connect automatically to your WiFi network.
You can use Ethernet, but I do not come from the past, so, I'm going to use a WiFi interface to use internet and connect my PC to the RapsberryPi using SSH.
Using your display and your external keyboard, follow these steps:
* Press `Windows` key to open the Menu.
* Open `Accessories > Terminal`
* `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
* Add this lines at the end of the file. PLEASE, fill it using the proper values (network name and network password)
```
network={
    ssid="The name of your wifi network"
    psk="The password"
}
```
* Exit saving (`Control + X`, `Y`, `ENTER`)
* Run `sudo ifdown wlan0` and `sudo ifup wlan0` (It will restart your WiFi device, so, it's going to connect to your WiFi network)
* Wait for a couple of seconds.
* Run `hostname -I`. That IP is your RaspberryPi IP in your WiFi network. It will be useful to connect using SSH, so, write it down in a paper.

Now, you are connected to your WiFi. From now, we going to use SSH to do all the remaining things.
You can disconnect your keyboard and display. We won't continue using them.

## Connect to RapsberryPi using SSH
Open your SSH client and connect to your RapsberryPi.

### For Mac users
* Open a Terminal
* `ssh YOUR_RASPBERRY_IP -l pi` (Example: `ssh 192.168.0.10 -l pi` or `ssh pi@192.168.0.10`)
* Password: `raspberry`

### For Windows users
[Feel free to send a Pull Request]

## Restart the RaspberryPi
In your SSH client:

* `sudo shutdown –r now`

Your RaspberryPi will close your connection, so, after one minute, reconnect your SSH again.

## Power Off the RaspberryPi
In your SSH client:

* `sudo shutdown –h now`

## Pre dependencies
Before starting working/playing with any project, you have to follow this stets to install basic software.
Run all this commands in your RaspberryPi.
* Update basic pre installed software `sudo apt-get update` and `sudo apt-get upgrade -y`. I recommend to DO NOT upgrade the distro, because the new one could be prepare to be used in a new RapsberryPi model (hardware), and you may have problems with some packages (yes, I had that problems).
* Basic software installation `sudo apt-get install -y curl git`

### Projects

#### SkyBroPy
Suite for PyInTheSky projects.
The community call `#PyInTheSky` all projects when in some way, you put your RaspberryPy in the sky for taking photos, or atmospheric measures.

### Projects comming
Nobody knows.