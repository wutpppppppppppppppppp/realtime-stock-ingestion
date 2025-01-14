from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

def main (spark):
    spark.sparkContext.setLogLevel("TRACE")

    # Step 2: Define Kafka Source
    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "broker:9092") \
        .option("subscribe", "stock_prices") \
        .option("startingOffsets", "latest") \
        .load()

    # Step 3: Define Schema for Incoming Data
    schema = StructType([
        StructField("symbol", StringType()),
        StructField("price", DoubleType()),
        StructField("timestamp", TimestampType())
    ])

    # Step 4: Parse JSON Messages
    parsed_df = kafka_df.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema).alias("data")) \
        .select("data.*")


    # Step 5: Perform Aggregation
    # Calculate the average price per symbol in a 10-second window
    aggregated_df = parsed_df.groupBy("symbol") \
        .agg(avg("price").alias("avg_price"))

    print(aggregated_df.avg_price)

    # Step 6: Write to Elasticsearch
    query = aggregated_df.writeStream \
        .outputMode("update") \
        .format("org.elasticsearch.spark.sql") \
        .option("es.nodes", "172.20.0.2") \
        .option("es.port", "9200") \
        .option("es.resource", "stocks/average_price") \
        .start()

    query.awaitTermination()

if __name__  == "__main__":
    # Step 1: Initialize Spark Session
    main(SparkSession.builder \
        .appName("KafkaSparkStreamingToElasticsearch") \
        .config("spark.master", "local[*]") \
        .config("spark.sql.streaming.checkpointLocation", "/tmp/spark-checkpoints") \
        .getOrCreate())