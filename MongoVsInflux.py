import pymongo
from influxdb import InfluxDBClient

import random
import time
import threading


# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["temperature"]

# Connect to InfluxDB
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')
client.create_database('test')


def writePoints():
    for x in range(10000):
        print(str(x))
        id = random.randrange(20, 40)
        value = random.randrange(20, 40)
        json_body = [
            {
                "measurement": "temperature",
                "tags": {
                    "id": id
                },
                "fields": {
                    "value": value
                }
            }
        ]
        client.write_points(json_body)

        json_body = {"id": id,"value": value}
        x = mycol.insert_one(json_body)



writePoints()
