# *Fogwing IoT Simulator Program for Raspberry Pi with Soil Moisture Sensor*

This directory provides two Python files that reads the data from Soil Moisture sensor and sends the same to Fogwing IoTHub.

**Note that these SDKs are currently in preview and are subject to change.**

## Hardware Instruction
* The CH0 -> CH7 pins are the analog inputs for MCP3008 from Soil Moisture Sensor. By default input to MCP3008 is CH2, following which you can change this pin to any Channel of MCP3008 by defining the same pin in code.
|     MCP3008    |    Raspberry PI     |
| -------------- |:-------------------:|
|   VDD (Pin 16) |       3.3V          |
|   VREF (Pin 15)|       3.3V          |
|   AGND (Pin 14)|      Ground         |
|   SCLK (Pin 13)| GPIO11(Pin 23/SCLK) |
|   MISO (Pin 12)| GPIO9 (Pin 21/MISO) |
|   MOSI (Pin 11)| GPIO10 (Pin 19/MOSI)|
|  CS/CE (Pin 10)| GPIO8 (Pin 24/CE0)  |
|  DGND (Pin 9)  |      Ground         |

## Fogwing IoT Simulation for DHT11
We have provided two python files:
* [Single Run - simulated_device_soilmoisture_single_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-soilmoisture-sensor/simulated_device_soilmoisture_single_run.py)

* [Interval Run - simulated_device_soilmoisture_interval_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-soilmoisture-sensor/simulated_device_soilmoisture_interval_run.py)

Both codes have the same logic. It collects data from Soil Moisture Sensor and sends it to Fogwing IoTHub. The only difference is that a single run sends data once and then stops, whereas an Interval run keeps sending data with every five minute gap until programs stop manually (Ctl+C).

**Do not use Interval Run for long run, it is better to use cron jobs or celery for a single run.**

## Step - 1
### Single Run or Interval Run
According to your requirement, copy any of the Python file to your raspberry and its good to go ! You now complete the coding part.

## Step - 2
### Installing the libraries
Install all required libraries using pip with our requirement.txt file.
```
pip install -r requirements.txt
```

## Step - 3
### Run and Get Started with Fogwing IoT
Change the client_id, username and password with your Fogwing IoTHub access credentials, after which you can run your file with the below command.
```
python file_name.py
```
Provided everything goes in line with the above mentioned instructions, you will be able to see a message that reads 'successfully published' in command line.

## Step - 4
### Start Analyzing your Data at Fogwing Community portal
Now you are ready to analyze your data at [Fogwing Community](http://community.fogwing.net/) portal, you can check all the data within the data logs in the portal.

## Getting help and finding Fogwing docs
* [Fogwing Community Forum]()
* [Fogwing Community Docs](https://docs.fogwing.io/)
