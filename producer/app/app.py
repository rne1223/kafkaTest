from flask import Flask, request
import logging
from time import sleep
from json import dumps
from kafka import KafkaProducer

app = Flask("__name__")

producer = KafkaProducer(bootstrap_servers=['kafka-0.kafka-headless.default.svc.cluster.local:9092'],
                        value_serializer=lambda x: 
                        dumps(x).encode('utf-8'))

logging.basicConfig(level=logging.DEBUG)

@app.route('/index')
def hello_world():
    msg = request.args.get('msg')

    if(msg is not None):
        data = {'message' : msg}
        producer.send('numtest',data)
        logging.info("Done Sending")
    
    # for e in range(10):
    #     data = {'number' : e}
    #     producer.send('numtest', value=data)
    #     sleep(1)

    return f"Send message: {msg}" 

if "__name__" == "__main__":
    app.run(host='0.0.0.0', port='30001', debug=True)