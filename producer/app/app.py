from sys import api_version
from flask import Flask, request
import logging
from time import sleep
from json import dumps
from kafka import KafkaProducer,errors

app = Flask("__name__")

producer = KafkaProducer(bootstrap_servers=['kafka-0.kafka-headless.default.svc.cluster.local:9092'],
                        value_serializer=lambda x: dumps(x).encode('utf-8'),
                        api_version=(0,10,1))

logging.basicConfig(level=logging.DEBUG)

@app.route('/index')
def hello_world():
    msg = request.args.get('msg')

    if(msg is not None):
        logging.info(msg)
        data = {"message" : f"{msg}"}
        producer.send('numtest3',data)
        producer.flush()
    

    return f"Send message: {msg}" 

if "__name__" == "__main__":
    app.run(host='0.0.0.0', port='30001', debug=True)