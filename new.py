import pymongo
import random
import time
import threading
from influxdb import InfluxDBClient


# Connect to MongoDB
myclientMongo = pymongo.MongoClient("mongodb://localhost:27017/")
mydbMongo = myclientMongo["teste"]
mycolMongo = myclientMongo["temperature"]

clientInflux = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')

start_time = time.time()
print("Starting InfluxDB...")

query_where = 'select count(*) from temperature where value=30;'
resultInflux = clientInflux.query(query_where)
print("Result: {0}".format(resultInflux))

print("Ending...")
print("--- %s seconds InfluxDB ---" % (time.time() - start_time))


start_time = time.time()
print("Starting MongoDB ...")


myquery = { "value": "30" }
#resultMongo = mycolMongo.find(myquery)
doc_count = mydbMongo.count_documents(myquery)
print("Result: {0}".format(resultMongo))

print("Ending...")

# Calculate time to write points
print("--- %s seconds MongoDB ---" % (time.time() - start_time))
