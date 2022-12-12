# During the night time, the computer will send you an email if the ISS is above your location on the globe.

import requests
from datetime import datetime
import smtplib
import time
import json
from PIL import Image  
import PIL  

f = open('emails.json')
data = json.load(f)

MY_EMAIL = ADD EMAIL HERE
def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if data["lat"]-30 <= iss_latitude <= data["lat"]+30 and data["long"]-30 <= iss_longitude <= data["long"]+30:
        return True

def nasa_potd():
    potd_response = requests.get(url="API GOES HERE")
    potd_response.raise_for_status()
    potd_data = potd_response.json()
    potd_image = float(potd_data["hdurl"])
    potd = Image.open(potd_image)  
    potd = potd.save("images/potd.png")

def is_night():
    parameters = {
        "lat": data["lat"],
        "lng": data["long"],
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


for data_set in data:
    time.sleep(60)
    if is_iss_overhead() and is_night() and data_set["hadIssRecently"] != 0:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        data_set["hadIssRecently"] = data_set["hadIssRecently"] + 1
        if data_set["hadIssRecently"] == 43200:
            data_set["hadIssRecently"] == 0
        #My_Password needs to be your real password from google 
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=data_set["email"],
            msg="Subject:Get ready, Look Up👆\n\nThe ISS is going to approach above you in the sky."
        )


f.close()
