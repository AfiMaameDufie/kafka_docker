from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9902")

topic = client.topics['sample']

# Creating a consumer
consumer = topic.get_simple_consumer()

# Go through messages for the topic: sample
for msg in consumer:
    if msg is not None:
        print(msg.offset, msg.value)