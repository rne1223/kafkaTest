import logging
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'numtest3',
    bootstrap_servers=['kafka.default.svc.cluster.local:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group3',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    api_version=(0,10,1))

logging.basicConfig(level=logging.DEBUG)

# logger.info("Hello World")

for message in consumer:
    for i in range(40):
        logging.info(message.value)
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