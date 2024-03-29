# *Fogwing IoT Simulator Program for Raspberry Pi with DHT11*

This directory provides two Python files that reads the data from DHT11 sensor and sends the same to Fogwing IoTHub.

**Note that these SDKs are currently in preview and are subject to change.**

## Hardware Instruction
We have used GPIO 2 of raspberry for this code to collect DHT11 sensor data. You need to connect your DHT11 sensor to GPIO 2 of raspberry, following which you can change this pin to any GPIO of Raspberry by defining the same pin in code.

## Fogwing IoT Simulation for DHT11
We have provided two python files:
* [Single Run - simulated_device_dht11_single_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-dht11-sensor/simulated_device_dht11_single_run.py)

* [Interval Run - simulated_device_dht11_interval_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-dht11-sensor/simulated_device_dht11_interval_run.py)

Both codes have the same logic. It collects data from DHT11 and sends it to Fogwing IoTHub. The only difference is that a single run sends data once and then stops, whereas an Interval run keeps sending data with every five minute gap until programs stop manually (Ctl+C).

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
### Start analyzing your data at Fogwing Platform
Now you are ready to analyze your data at [Fogwing Platform](https://portal.fogwing.net/) portal, you can check all the data within the data logs in the portal.

## Getting help and finding Fogwing docs
* [Fogwing Forum](https://community.fogwing.io/)
* [Fogwing Docs](https://docs.fogwing.io/)
