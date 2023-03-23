import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("RPI3")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("DateTime")
client.on_message = on_message
time.sleep(30)
client.loop_end()