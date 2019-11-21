''' * Copyright (C) 2019 Factana Computing Pvt Ltd.
    * All Rights Reserved.
    * This file is subject to the terms and conditions defined in
    * file 'LICENSE.txt', which is part of this source code package.'''

import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt

# Do not change Fogwing IoT Hub host, port and topic
host_name = 'iothub.community.fogwing.net'
port = 8883
topic = 'fwcom/inbound/edge/data'

# Use your Fogwing IoT Hub access credentials
client_id = 'your_Fogwing_IoTHub_clientid'
username = 'your_Fogwing_IoTHub_username'
password = 'your_Fogwing_IoTHub_password'
dev_eui = 'your_Fogwing_IoTHub_deveui'


# Function gets the data from dht11 sensor and returns teperature and humidity
def temphum():
    dht = 11
    th = 2  # GPIO 2 of raspberry pi
    humidity, temperature = Adafruit_DHT.read_retry(dht, th)
    return humidity, temperature


result_temphum = temphum()

humidity = result_temphum[0]
temperature = result_temphum[1]

# Define the JSON message to send to Fogwing IoT Hub
message = { "client_id": client_id, "dev_eui": dev_eui,
            "payload": { "Temperature": temperature,
                         "Humidity": humidity,
                }
    }


# The callback for when the client disconnect from the server.
def on_disconnect(client, userdata, rc):
    if rc == 0:
       print("Fogwing IoT Hub: Client disconnected")
       client.connected_flag = False


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("Fogwing IoT Hub: Successfully connected")
        print("Fogwing IoT Hub: Successfully message published ")
    elif rc == 1:
        print("Fogwing IoT Hub: Unacceptable protocol version of Fogwing IoT Hub")
    elif rc == 2:
        print("Fogwing IoT Hub: Invalid client identifier")
    elif rc == 3:
        print("Fogwing IoT Hub: Server is unavailable to connect")
    elif rc == 4:
        print("Fogwing IoT Hub: Bad username or password or client_id")
    elif rc == 5:
        print("Fogwing IoT Hub: You are not authorised to connect")
    elif rc == 6:
        print("Fogwing IoT Hub: Currently server is unused")


# The callback for when the client receives a Messageid response from the server.
def on_publish(client, userdata, mid, qos=1):
    print("Fogwing IoT Hub: mid value is {} and qos value is {}".format(mid, qos))


# The callback for when the client receives a log response from the server.
def on_log(client, userdata, level, buf):
    print("Fogwing IoT Hub: " + buf)


client = mqtt.Client(client_id, clean_session=True)
client.username_pw_set(username=username, password=password)
client.tls_set_context(context=None)
client.on_connect = on_connect
client.on_log = on_log
client.on_publish = on_publish
client.on_disconnect = on_disconnect


# Making connection to Fogwing IoTHub with provided host_name
def Fogwing_IoTHub_client_telemetry_run():
    try:
        client.connect(host_name, port=8883, keepalive=60)
    except Exception as ex:
        print("Fogwing IoT Hub: Connection failed: ", ex)
    except KeyboardInterrupt:
        print("Fogwing IoT Hub: DHT11 stopped")

    client.loop_start()
    client.publish(topic, json.dumps(message))
    time.sleep(1)
    client.loop_stop()


if __name__ == '__main__':
    print("Fogwing IoT Hub: Started to connecting...")
    print("Fogwing IoT Hub: Press Ctrl+C to exit")
    Fogwing_IoTHub_client_telemetry_run()
