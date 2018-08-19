"""
The following code is modified from 
https://jamesooi.bitbucket.io/UEEN3123/lectures/UEEN3123-Lecture-04-i.html
"""
import socket
import re
import time
import json
from datetime import datetime

PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def getData():
    return json.dumps({
        "dateOfOccurence": getDateOfOccurence(),
        "timeOfOccurence": getTimeOfOccurence(),
        "warningType"    : getWarningType(),
        "location"       : input("Enter location: "),
        "description"    : input("Enter description: "),
        "createdAt"      : str(datetime.now())
    })

def getDateOfOccurence():
    # Modified from https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
    while True:
        date = input("Enter date of occurence (YYYYMMDD): ")
        try:
            return str(datetime.strptime(date, '%Y%m%d'))
        except ValueError:
            print("Incorrect data format, should be YYYYMMDD.\n")

def getTimeOfOccurence():
    while True:
        time = input("Enter time of occurence in 24h format (HHMM): ")
        r = re.compile("([0-1][0-9]|[2][0-4])[0-5][0-9]")
        if r.match(time):
            return time
        else:
            print("Incorrect time format.\n")

def getWarningType():
    while True:
        t = input("Enter type (Earthquake[E]/Tsunami[T]): ")
        if t.lower() in ['e' , 't']:
            return {'e': 'Earthquake', 't': 'Tsunami'}[t.lower()]
        else:
            print("Error. Should be E or T.\n")

if __name__ == "__main__":
    while True:
        response = getData()
        s.sendto(response.encode(), ('<broadcast>', PORT))
        print('[+] Broadcasted data to UDP port {}'.format(PORT))
        ans = input("Enter new data? ([Y]/n) ")
        if ans == "n":
            exit(0)
