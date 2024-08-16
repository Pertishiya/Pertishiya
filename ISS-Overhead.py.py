import requests
from datetime import datetime
import time
import smtplib

MY_EMAIL = "***@gmail.com"
MY_PASSWORD = "***"

MY_LAT = 120.507351 # Your latitude
MY_LONG = -55.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        print("ISS is near")
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >=sunset or time_now <=sunrise:
        print("Its dark outside!!")
        return True

while True:
    print("Checking...")
    time.sleep(6)
    is_iss_overhead()
    is_night()
    if is_iss_overhead() and is_night():
        print("ISS above you in the sky")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
            msg = "Subject: Look up ☝️ \n\nThe ISS is above you in the sky."
        )




