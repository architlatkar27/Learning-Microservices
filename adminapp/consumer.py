import pika, json
params = pika.URLParameters("amqps://etekuqpe:dTvC4l2EA3pn-Fw2OrqnVE36ZXq-44UG@hornet.rmq.cloudamqp.com/etekuqpe")

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue="admin")

def callback(ch, method, properties, body):
    print("Recieve in admin")
    print(body)

channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)
print("Started consuming")

channel.start_consuming()
channel.close()