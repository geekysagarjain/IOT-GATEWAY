# publisher
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('35.154.105.25', 1883)

while True:
    client.publish("LINTANGtopic/test", input('Message : '))