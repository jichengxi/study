from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='172.17.36.201:9092')
for i in range(10):
    msg = "this massages is " + str(i)
    producer.send('test', msg.encode('utf-8'))
producer.close()