# producer.py
import os, random, time, json
from confluent_kafka import Producer

p = Producer({"bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")})

while True:
    payload = {
        "id":   f"sensor-{random.randint(1,5)}",
        "ts":   int(time.time()),
        "temp": round(random.uniform(20,30), 2)
    }
    p.produce("raw-sensor-data", json.dumps(payload))
    p.flush()
    print(payload)
    time.sleep(1)

