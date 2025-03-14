from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaStream") \
    .getOrCreate()

# Kafka configuration
KAFKA_BROKER = "localhost:9092"  # Your Kafka broker address
KAFKA_TOPIC = "your-topic"  # The Kafka topic you're streaming from
spark.sparkContext.setLogLevel("ERROR")

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe", KAFKA_TOPIC) \
    .load()

# The Kafka message is stored in the 'value' column, and it's in binary format.
# Convert the binary 'value' column to string (assuming the message is in JSON format)
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Define the schema for the JSON message
schema = StructType([
    StructField("title", StringType(), True),
    StructField("body", StringType(), True)
])

# Parse the JSON data
df = df.selectExpr("key", "CAST(value AS STRING) as json_value") \
    .select(from_json("json_value", schema).alias("data"))

# Extract the individual fields from the parsed JSON
df = df.select("data.title", "data.body")

# Write the streaming DataFrame to the console for debugging (you can write to other sinks like Kafka, S3, etc.)
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Await termination of the stream
query.awaitTermination()