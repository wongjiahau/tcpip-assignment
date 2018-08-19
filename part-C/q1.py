"""
The following code is modifed from
https://jamesooi.bitbucket.io/UEEN3123/lectures/UEEN3123-Lecture-05.html
"""
import http.client
import json
import csv


HOST = 'localhost'
PORT = 5000

print('### Connecting to {}:{}'.format(HOST, PORT))
conn = http.client.HTTPConnection(HOST, PORT)

with open('q1.csv') as file:
    members = csv.DictReader(file)
    for member in members:
        member = dict(member)

        print('### Sending HTTP Request')
        conn.request('POST', '/api/stations', json.dumps(member), {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        })

        print('### HTTP Response Received')
        response = conn.getresponse()

        if response.status == 201:
            result = json.loads(response.read())
            print(result)
        else:
            print('### ERROR: {}'.format(response.status))