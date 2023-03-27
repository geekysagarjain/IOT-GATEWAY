import logging
import asyncio
from hbmqtt.broker import Broker
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1
    
logger = logging.getLogger(__name__)

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
            print(packet.payload.data.decode('utf-8'))
    except ClientException as ce:
        logger.error("Client exception : %s" % ce)

if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(brokerGetMessage())
    asyncio.get_event_loop().run_forever()