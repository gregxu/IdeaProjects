import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print ('[*] waiting for messages. ')

def callback(ch, method, properties, body):
    print(" [x] received %r" % (body,))

channel.basic_consume(callback, queue=queue_name, no_ack=True)


channel.start_consuming()