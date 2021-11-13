from kafka import KafkaConsumer
consumer = KafkaConsumer('test', bootstrap_servers='172.17.36.203')
for msg in consumer:
    print(msg)