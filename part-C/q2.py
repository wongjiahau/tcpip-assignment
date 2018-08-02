"""
The following code is modifed from
https://jamesooi.bitbucket.io/UEEN3123/lectures/UEEN3123-Lecture-05.html
"""
import http.client
import json
import csv


HOST = 'localhost'
PORT = 5000

print('>>> Connecting to {}:{}'.format(HOST, PORT))
conn = http.client.HTTPConnection(HOST, PORT)

print('>>> Sending HTTP Request to http://localhost:5000/api/stations')
conn.request('GET', '/api/stations')

print('>>> HTTP Response Received')
response = conn.getresponse()

if response.status == 200:
    members = json.loads(response.read())

    print('>>> Writing data to retrieved_stations.csv')
    with open('retrieved_stations.csv', 'w', newline='') as file:
        fields = [ 'id', 'code', 'name', 'type']
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()

        for member in members:
            writer.writerow(member)

        print('>>> Writing completed!')
else:
    print('>>> ERROR: {}'.format(response.status))