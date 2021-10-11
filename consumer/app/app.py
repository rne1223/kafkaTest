import logging
from kafka import KafkaConsumer
from json import loads
import sys,os

# logger = logging.getLogger("__name__")
logging.basicConfig(level=logging.CRITICAL)
# h1 = logging.StreamHandler(sys.stdout)
# h1.setLevel(logging.DEBUG)
# logger.addHandler(h1)

consumer = KafkaConsumer(
    'numtest2',
    bootstrap_servers=['kafka.default.svc.cluster.local:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group2',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    api_version=(0,10,1))

# logger.info("Hello World")
logging.info("this is a test")
for i in range(40):
    logging.info("Hello World")

for message in consumer:
    print("inside")
    # logger.info("Test")
    message = message.value
    print(message)
    # print(f"Got message: {message}")
    # logger.info(f"Got message: {message}")

for i in range(4):
    print("Fool")

if "__name__" == "__main__":
    print("Entered")
    # logger.info("Consumer Started")

#  kafka-console-producer.sh --broker-list kafka-0.kafka-headless.default.svc.cluster.local:9092 --topic numtest 
#  kafka-console-consumer.sh --bootstrap-server kafka.default.svc.cluster.local:9092 --topic numtest --from-beginning