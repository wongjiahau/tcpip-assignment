"""
The following code is modified from 
https://jamesooi.bitbucket.io/UEEN3123/lectures/UEEN3123-Lecture-04-i.html
"""

import socket
import json

PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', PORT))

def displayData(propertyName, propertyValue):
    print(f"{propertyName} : {propertyValue}" )

while True:
    data, addr = s.recvfrom(1024)
    data = json.loads(data.decode())
    print("=======================================================")
    displayData("Received on      ", data['createdAt'])
    displayData("Date of occurence", data['dateOfOccurence'])
    displayData("Time of occurence", data['timeOfOccurence'])
    displayData("Warning type     ", data['warningType'])
    displayData("Location         ", data['location'])
    displayData("Description      ", data['description'])
    print("=======================================================")


