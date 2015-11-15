from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
es = Elasticsearch(['es'])

while True:
	for message in consumer:
		new_listing = json.loads(message.value.decode())
		es.index(index='listing_index', doc_type='listing', id=new_listing['id'], body=new_listing)
		es.indices.refresh(index="listing_index")
		print(new_listing)
