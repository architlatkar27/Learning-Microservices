# amqps://etekuqpe:dTvC4l2EA3pn-Fw2OrqnVE36ZXq-44UG@hornet.rmq.cloudamqp.com/etekuqpe

import pika, json
params = pika.URLParameters("amqps://etekuqpe:dTvC4l2EA3pn-Fw2OrqnVE36ZXq-44UG@hornet.rmq.cloudamqp.com/etekuqpe")

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)
