# *Fogwing IoT Simulator Program for Raspberry Pi with DHT11*

This directory provides two Python file that reads the data from DHT11 sensor and sends to Fogwing IoTHub.

**Note that these SDKs are currently in preview and are subject to change.**

## Hardware Instruction
We have used GPIO 2 of raspberry for this code to collect DHT11 sensor data, so you need to connect your DHT11 sensor to GPIO 2 of raspberry. You can change this pin to any GPIO of Raspberry by defining same pin in code.

## Fogwing IoT Simulation for DHT11
We have provided two python files:
* [Single Run - simulated_device_dht11_single_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-dht11-sensor/simulated_device_dht11_single_run.py)

* [Interval Run - simulated_device_dht11_interval_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-dht11-sensor/simulated_device_dht11_interval_run.py)

Both code has same logic that collects data from DHT11 and sends it to Fogwing IoTHub. Only difference is single run sends data once and then it stops but Interval run keeps sending data for each five minute until programs stops manually (Ctl+C).

**Do not use Interval Run for long run, it is better to user cron jobs or celery with single run**

## Step - 1
### Single Run or Interval Run
According to your requirement copy any of the Python file to your raspberry and thats it ! Your are now done with coding part.

## Step - 2
### Installing the libraries
Install all required libraries using pip with our requirement.txt file.
```
pip install -r requirements.txt
```

## Step - 3
### Run and Get Started with Fogwing IoT
Change the client_id, username and password with your Fogwing IoTHub access credentials, after this change you can run your file with below command.
```
python file_name.py
```
If everything goes well you will be seeing successfully published message in command line.

## Step - 4
### Start Analyzing your Data at Fogwing Community portal
Now you are ready to analyze your data at [Fogwing Community](http://community.fogwing.net/) portal, you can check all the data in data logs inside the portal.

## Getting help and finding Fogwing docs
* [Fogwing Community Forum]()
* [Fogwing Community Docs](https://docs.fogwing.io/)
