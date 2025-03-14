# 🚀 Kafka API with PySpark & Docker

**Real-time Data Streaming with Apache Kafka, PySpark, and FastAPI**

## 📌 Overview  
This project provides a **real-time streaming API** using **FastAPI**, **Apache Kafka**, and **PySpark Structured Streaming**. It enables seamless data ingestion, processing, and consumption in a **Dockerized** environment.  

## 🛠️ Tech Stack  
- **FastAPI** For building the REST API  
- **Apache Kafka** For real-time message streaming  
- **PySpark** For real-time data processing  
- **Docker** To containerize the application  


## Prerequisites
- **Docker & Docker Compose** installed on your machine
- **Pyspark**

## 🚀 Features  
- ✔️ **Publish messages** to Kafka via FastAPI
- ✔️ **Consume messages** using PySpark Structured Streaming in realtime 
- ✔️ **Dockerized** setup for easy deployment 

## 🏗️ Setup & Installation  

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/ItisVenkatesh/api-kafka-pyspark-docker.git
cd api-kafka-pyspark-docker
```

### 🔹 2. Start Docker  
Start docker engine. Then start the container for kafka using docker-compose.

```bash
docker-compose up --build -d
```

### 🔹 3. Install Dependencies  
Install the dependent libraries using below command.

```bash
pip install -r requirements.txt
```

### 🔹 4. Start Kafka Producer  
Start the Kafka producer API using uvicorn.

```bash
cd src
uvicorn fastapi_kafka_producer:app --host 0.0.0.0 --port 8000
```

### 🔹 5. Send a test message to Kafka
In a separate terminal window,

```bash
curl -X POST "http://localhost:8000/publish" -H "Content-Type: application/json" -d '{"title": "Kafka Sample Message", "body": "My test message"}'
```

You should see an output like below.
{"message":"Message sent to Kafka successfully","data":{"title":"Kafka Sample Message","body":"My test message"}}

Also, in the uvicorn window, you should see a log like below.
INFO:     127.0.0.1:50089 - "POST /publish HTTP/1.1" 200 OK

### 🔹 6. Start Kafka Consumer  
Kafka Consumer is nothing but kafka_streaming.py program. 

In a separate terminal window,
```bash
cd src
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 kafka_streaming.py
```
It produces Spark logs in this terminal window.

### 🔹 7. Send a message to Kafka
In a separate terminal window,

```bash
curl -X POST "http://localhost:8000/publish" -H "Content-Type: application/json" -d '{"title": "Your Message Title", "body": "Your realtime message"}'
```

### 🔹 7. Streaming in realtime  
View the pyspark logs to check the posted message. You can also change the code to write into an output database table or dataset.

### 🔹 8. To stop streaming
- Press [ctrl + c] in uvicorn terminal to stop uvicorn server.
- Press [ctrl + c] in spark terminal to stop the streaming spark job.
- To stop Docker containers,

```bash
docker-compose down
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

❤️ Venkatesh Shankar.