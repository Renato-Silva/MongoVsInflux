import pymongo
import random
import time
import threading


# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["teste"]
mycol = mydb["temperature"]

def writePoints():
    for x in range(1000):
        print(str(x))
        json_body = {"id": random.randrange(20, 40),"value": random.randrange(20, 40)}

        # Write point
        x = mycol.insert_one(json_body)


# Save starting time
start_time = time.time()
print("Starting...")

writePoints()

print("Ending...")

# Calculate time to write points
print("--- %s seconds ---" % (time.time() - start_time))
