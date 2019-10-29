from influxdb import InfluxDBClient
import random
import time
import threading

# Connect to InfluxDB
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')

# Create a database
client.create_database('test')

def writePoints():
    for x in range(1000000):
        print(str(x))
        json_body = [
            {
                "measurement": "temperature",
                "tags": {
                    "id": random.randrange(20, 40)
                },
                "time": 1472666050+x,
                "fields": {
                    "value": random.randrange(20, 40)
                }
            }
        ]

        # Write point
        client.write_points(json_body)


# Save starting time
start_time = time.time()
print("Starting...")

writePoints()


print("Ending...")

# Calculate time to write points
print("--- %s seconds ---" % (time.time() - start_time))
