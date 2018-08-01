"""
The following code is modified from 
https://jamesooi.bitbucket.io/UEEN3123/lectures/UEEN3123-Lecture-04-i.html
"""
import socket
import time
import json
from datetime import datetime

PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def getData():
    dateOfOccurence = float(input("Enter date of occurence :"))
    timeOfOccurence = float(input("Enter time of occurence :"))
    warningType     = float(input("Enter type (Earthquake/Tsunami Warning) :"))
    location        = float(input("Enter location :"))
    description     = float(input("Enter description :"))
    return json.dumps({
        "dateOfOccurence": dateOfOccurence,
        "timeOfOccurence": timeOfOccurence,
        "warningType"    : warningType,
        "location"       : location,
        "description"    : description,
        "createdAt"      : str(datetime.now())
    })

while True:
    response = getData()
    s.sendto(response.encode(), ('<broadcast>', PORT))
    print('[+] Broadcasted data to UDP port {}'.format(PORT))
    ans = input("Enter new data? ([Y]/n) ")
    if ans == "n":
        exit(0)
