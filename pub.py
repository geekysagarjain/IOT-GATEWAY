# publisher
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('35.154.105.25', 1883)
ble = {'area_uuid': 51,
 'created_at': '11/12/2023',
 'node_name': 'washroom-light',
 'node_product_id': 5555,
 'node_status': 'off',
 'node_type': 'light',
 'node_uuid': 4444,
 'node_vendor_id': 9999,
 'project_uuid': 1111,
 'zone_uuid': 2222}

client.publish("connect", str(ble))