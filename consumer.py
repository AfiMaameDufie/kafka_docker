from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9902")

topic = client.topics['sample']

# Creating a consumer
consumer = topic.get_simple_consumer()