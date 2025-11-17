#!/usr/bin/python3
import pika


localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.queue_delete(queue='rpc_queue')
channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        body=str(response),
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=on_request, queue='rpc_queue')

print("[*] Waiting for messages. press Ctrl+C to exit")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\nStopping server...")
    connection.close()
