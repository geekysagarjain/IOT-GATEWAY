import paho.mqtt.client as mqtt
import time

fp= open(r'/home/pi/serial-data.txt', 'r')
content = fp.readlines()

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("DateTime")
client.connect(mqttBroker)

while True:
    client.publish("DateTime", str(content))
    print("Published The MSG")
    time.sleep(1)