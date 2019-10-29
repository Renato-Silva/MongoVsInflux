import csv
import pymongo
from influxdb import InfluxDBClient


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mysense"]
mycol = mydb["col1"]


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')
client.create_database('test')


for x in range(10):
    with open('sense.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("First line")
                line_count += 1
            else:
                a = {"day": row[0],"time": row[1], "vwc": row[2],"adc2": row[3], "temp": row[4], "rhum": row[5],"solar": row[6], "cjt": row[7],"granier": row[8],"heater":row[9] ,"bat":row[10]}
                print(a)
                json_body = [{
                    "measurement": "test1",
                    "tags": {
                        "id":1
                    },
                    "fields": {
                        "vwc": float(row[2]),"adc2": float(row[3]), "temp": float(row[4]), "rhum": float(row[5]),"solar": float(row[6]), "cjt": float(row[7]),"granier": float(row[8]),"heater": float(row[9]) ,"bat":float(row[10])
                    }
                }]

                client.write_points(json_body)
                #x = mycol.insert_one(json_body)
                line_count += 1
        print(f'Processed {line_count} lines.')
