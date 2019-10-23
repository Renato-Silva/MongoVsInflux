from influxdb import InfluxDBClient
import random
import time
import threading

# Connect to InfluxDB
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')

# Create a database
#client.create_database('test')

def writePoints():
    for x in range(100000):
        json_body = [
            {
                "measurement": "temperature",
                "tags": {
                    "id": random.randrange(20, 40)
                },
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


t1 = threading.Thread(target=writePoints, args=())
t2 = threading.Thread(target=writePoints, args=())
t3 = threading.Thread(target=writePoints, args=())
t4 = threading.Thread(target=writePoints, args=())
t5 = threading.Thread(target=writePoints, args=())
t6 = threading.Thread(target=writePoints, args=())
t7 = threading.Thread(target=writePoints, args=())
t8 = threading.Thread(target=writePoints, args=())
t9 = threading.Thread(target=writePoints, args=())
t10 = threading.Thread(target=writePoints, args=())


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()


print("Ending...")

# Calculate time to write points
print("--- %s seconds ---" % (time.time() - start_time))
