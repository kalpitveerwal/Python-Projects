import urllib.request
import json
from datetime import datetime


def iss_location():
    with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as url:
        data = json.loads(url.read().decode())
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
    print("Current Location of ISS:")
    print("Latitude : " + str(lat))
    print("Longitude : " + str(lon))


def pass_time(lat, lon):
    address = "http://api.open-notify.org/iss-pass.json" + "?lat=" + str(lat) + "&lon=" + str(lon)
    with urllib.request.urlopen(address) as url:
        data = json.loads(url.read().decode())
        duration = data['response'][0]['duration']
        time = data['response'][0]['risetime']
    p = datetime.fromtimestamp(time)
    minute = int(duration/60)
    second = (duration % 60)
    print("Date : " + str(p.day).zfill(2) + "/" + str(p.month).zfill(2) + "/" + str(p.year))
    print("Time : " + str(p.hour).zfill(2) + ":" + str(p.minute).zfill(2))
    print("For : " + str(minute) + " minutes and " + str(second) +  " seconds")


def people_info():
    with urllib.request.urlopen("http://api.open-notify.org/astros.json") as url:
        data = json.loads(url.read().decode())
        total_no = data['number']
        i = 0
        people = []
        while i < total_no :
            people.append(data['people'][i]['name'])
            i = i + 1
        print("People currently in space: " + str(total_no))
        j = 0
        while j < total_no:
            print(str(j + 1) + ". " + people[j])
            j = j + 1

            
iss_location()

print("Enter Details to know when ISS will pass over a location:")
lat = input("Latitude : ")
lon = input("Longitude : ")

pass_time(lat, lon)

people_info()
