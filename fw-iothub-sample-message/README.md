# *Fogwing IoT Simulator Program for Raspberry Pi with sample message*

This directory provides two Python files that send sample messages to Fogwing IoTHub.

**Note that these SDKs are currently in preview and are subject to change.**

## Fogwing IoT Simulation for DHT11
We have provided two python files:
* [Single Run - simulated_device_message_single_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-sample-message/simulated_device_message_single_run.py)

* [Interval Run - simulated_device_message_interval_run.py](https://github.com/factana/fogwing-simulator-for-raspberry-python/blob/master/fw-iothub-sample-message/simulated_device_message_interval_run.py)

Both codes have the same logic that sends sample messages to Fogwing IoTHub. Only difference is that a single run sends data once and then it stops whereas an Interval run keeps sending data with every five minute gap until programs stops manually (Ctl+C).

**Do not use Interval Run for long run, it is better to use cron jobs or celery with single run.**

## Step - 1
### Single Run or Interval Run
According to your requirement, copy any of the Python files to your raspberry and you are good to start ! You now finish with coding part.

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
Provided everything goes in line with the above mentioned instructions you will be able to see a message that reads 'successfully published' in the command line.

## Step - 4
### Start Analyzing your Data at Fogwing Platform
Now you are ready to analyze your data at [Fogwing Platform](https://enterprise.fogwing.net/) portal, you can check all data in the data logs within the portal.

## Getting help and finding Fogwing docs
* [Fogwing Platform Forum]()
* [Fogwing Platform Docs](https://docs.fogwing.io/)
