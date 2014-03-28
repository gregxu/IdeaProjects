import pika
import sys

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', type='fanout')

    message = "info: Hello World!"

    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print (" [x] Sent %r" % (message,))

    connection.close()

send_message()