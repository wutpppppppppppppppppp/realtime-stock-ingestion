# Build Docker images
build:
	docker build -t spark-job ./spark
	docker build -t kafka-producer ./producer
	docker compose build

# Start all services and create Kafka topic
start:
	docker compose up -d
	docker exec -it broker /opt/kafka/bin/kafka-topics.sh \
	  --create --topic stock_prices --bootstrap-server broker:9092 \
	  --partitions 1 --replication-factor 1 || true

# Stop all services
stop:
	docker compose down

logs-broker:
	docker logs -f broker

logs-producer:
	docker logs -f python_producer

logs-spark:
	docker logs -f spark

logs-elastic:
	docker logs -f elasticsearch
