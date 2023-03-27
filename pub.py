# publisher
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('35.154.105.25', 1883)
ble = "connected to device 1"

client.publish("connect", ble)