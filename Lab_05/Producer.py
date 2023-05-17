import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')

while True:
    message = str(int(time.time()))
    producer.send('common', value=message.encode('utf-8'))
    print(f'Sent message: {message}')
    time.sleep(5)