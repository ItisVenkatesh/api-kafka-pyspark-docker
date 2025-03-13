from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json

# Initialize FastAPI app
app = FastAPI()

# Kafka configuration
KAFKA_SERVER = 'localhost:9092'  # Adjust this to your Kafka server's address
KAFKA_TOPIC = 'your-topic'  # Replace with your Kafka topic

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize message to JSON
)

# Pydantic model for input data
class Message(BaseModel):
    title: str
    body: str

@app.post("/publish")
async def post_message(data: Message):
    # Sending the message to Kafka
    producer.send(KAFKA_TOPIC, value=data.dict())
    producer.flush()  # Ensure the message is sent immediately
    
    return {"message": "Message sent to Kafka successfully", "data": data.dict()}