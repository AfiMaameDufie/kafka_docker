from pykafka import KafkaClient

# Create a Kafka Client
client = KafkaClient(hosts="localhost:9092")

# Get the "sample" topic
topic = client.topics['sample']

# Create a producer
producer = topic.get_sync_producer()