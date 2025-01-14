# Kafka-Spark-Elasticsearch Project

This project demonstrates the integration of Apache Kafka, Apache Spark, and Elasticsearch for real-time data processing and analytics.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases a pipeline where data is ingested through Kafka, processed using Spark, and stored in Elasticsearch for further analysis and visualization.

## Prerequisites

- Docker and Docker Compose
- Python (optional, for additional scripts)

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/kafka-spark-elasticsearch.git
   cd kafka-spark-elasticsearch
   ```

2. **Build Docker images:**

   ```sh
   make build
   ```

3. **Start all services and create Kafka topic:**

   ```sh
   make start
   ```

## Usage

1. **Monitor the data flow:**
   - Use Kafka tools to monitor the topics.
   - Use Kibana or another Elasticsearch client to visualize the data.

2. **View logs:**
   - Kafka Broker: `make logs-broker`
   - Kafka Producer: `make logs-producer`
   - Spark: `make logs-spark`
   - Elasticsearch: `make logs-elastic`

3. **Stop all services:**

   ```sh
   make stop
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
