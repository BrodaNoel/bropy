# BroPy
BroPy, a full suite for RaspberryPi control.
Each project and module have its own folder and documentation.

Sorry for my english. Feel free to send Pull Request fixing my languaje mistakes (do not touch my code... you will die mother f... just kidding. Create issues or PR as you want! It's free! Woho!).

## You have to know, before starting
* The RaspberryPi used for this project, is `RaspberryPi 2 Model B` (https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)
* Your RaspberryPi should use `NOOBS` (https://www.raspberrypi.org/downloads/noobs/) with `Rapsbian Jessie`.
* We recommend restart your RaspberryPi SO before follow the guide (read more about it in next steps)
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
* `ssh pi@YOUR_RASPBERRY_IP` (Example: `ssh pi@192.168.0.10`)
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
* Remove unused packages `sudo apt-get autoremove -y`

## Install BroPy in your RaspberryPi
It doesn't matter if you only will use one of all the BroPy projects. We recommend to install/clone all BroPy in your RaspberryPi. Follow this steps:
* Move to `~` running `cd`. (If you change this folder, you may have problems.)
* `git clone https://github.com/BrodaNoel/bropy.git`
* `./install.sh`
* Done. Now, BroPy is installed in `~/bropy`.

## Learning BroPy. How it works?
You have to think BroPy is a module and project container.

A `module` can be a hardware to measure temperature, or a GPS, or a camera, and also can be something non-hardware-related, like a Math library, or a Map drawer, or can by a library to get the temperature from some internet-service. So, as you can see, you can get the temperature using a hardware module, or a software module.

A `project` is just a way to implement/use/play with modules.
For example, we can have a project in charge of measure the temperature in your city and send it you by email.


Let's supouse we want to create a project to send you the temperature of your city by email. We'll call it "TheFancyTemperatureMeasurer"
As you know, we can measure the temperature using a software or hardware module. So, what we should do, is code the project implementing abstractions about or modules.
It doesn't matter how the module works. You know that a temperature measure module should give you a value called "temperature" (and maybe more data, but, let's just pay attention in this one). And in another hand you know that the module to send emails should give you kind of basic behavior to say: "Ok, send THIS TEXT to THIS EMAIL. Thanks".
In order to create this project, you should create a folder called `TheFancyTemperatureMeasurer`, into `projects` folder.
So, the really-basic-non-functional-code of our project should be something like:
```javascript
import temperature-module;
import email-module;

var temperature = temperature-module.getTemperature();
email-module.sendEmail('bropy@bropy.com', 'The email subject', 'The temperature is ' + temperature);
```
Easy, right? But, how we will define which module should we use? Because, remember we can get the temperature from different modules created for this (why? well, you can buy lot of differents temperture measurer and all of them work differently).

Let's supouse you bought your RaspberryPi and a temperature measurer called "temp-0123". The first thing you have to do, is go to `modules` folder, and check if someone already create the module (the driver) for your module. If no one did it, you have to do it (or just create an issue and we can Google something for you), BUT, if you have luck, maybe someone did it, and you just have to use it.

Projects just define HOW things should works, but it doesn't define WHICH module should be implemented to do it. So, the code we created a few minutes ago, is enough for us, and now we just need to run it defining which module should implement. How to do it? Easy, you have to say something like: "Hey BroPy, let's run the `TheFancyTemperatureMeasurer`, using the `temp-0123` and `email` module". As you should be thinking right now, we must have crated a module called `email` inside the `modules` folder. So, in you *terminal*, run:
`bropy -p TheFancyTemperatureMeasurer -m temp-0123,email`

* `-p` means "project"
* `-m` means "modules", and all of them should be separated by comma, with no spaces.

Obviously it's not all things you have to do to create a project. If you want to learn in deep how to do it, check the `creating-a-project.md` file.

If you just want to use an already created project, just go to read the Project documentation (`README.md` file inside the project folder). In that file you should have all the information related to how to run the project, which modules are compatible, and more.

We hope you get fun here!


### Projects

#### BroPySky
Suite for PyInTheSky projects.
The community call `#PyInTheSky` all projects when in some way, you put your RaspberryPy in the sky for taking photos, or atmospheric measures.

### Projects comming
Nobody knows. If you have an idea, create an Issue and we'll create it!