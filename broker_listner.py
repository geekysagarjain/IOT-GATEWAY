import logging
import asyncio
from hbmqtt.broker import Broker
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1
from pymongo import MongoClient
import ast
    
logger = logging.getLogger(__name__)

client = MongoClient('localhost', 27017) #creating mongodb client connection
db = client.practice #connecting to the mongodb practice database 

def insertDocumentDb(receivedData, receivedCollection): #to insert a document in the db
    collection = db[receivedCollection]
    collection.insert_one(receivedData)

def detectCollection(receivedData):
    if "node_name" in receivedData:
        print(receivedData["node_name"])


@asyncio.coroutine
def brokerGetMessage():
    C = MQTTClient()
    yield from C.connect('mqtt://0.0.0.0:1883/')
    yield from C.subscribe([
        ("scan", QOS_1), ("connect", QOS_1), ("led_on", QOS_1), ("led_off", QOS_1)
    ])
    logger.info('Subscribed!')
    try:
        for i in range(1,100):
            message = yield from C.deliver_message()
            packet = message.publish_packet
            mqtt_received_data=packet.payload.data.decode('utf-8') #decoding the data to string
            mqtt_jsonified=ast.literal_eval(mqtt_received_data) #converting str to dict
            detectCollection(mqtt_jsonified)
    except ClientException as ce:
        logger.error("Client exception : %s" % ce)

if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(brokerGetMessage())
    asyncio.get_event_loop().run_forever()