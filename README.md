# Project Title


## Installation


## Usage


uvicorn fastapi_kafka_producer:app --host 0.0.0.0 --port 8000

spark-submit \
    --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 \
    kafka_streaming.py

curl -X POST "http://localhost:8000/publish" -H "Content-Type: application/json" -d '{"title": "Kafka Message", "body": "Hello Kafka!"}'

## License

