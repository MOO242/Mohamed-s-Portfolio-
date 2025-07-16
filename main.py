import requests
import datetime as dt
import time
import smtplib

""" My location """

MY_LAT = 25
MY_LNG = 55

par = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

""" ISS Location """


def get_iss_location():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5
    ):
        return True


""" SunRise in my LOC"""


def sunrise():

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=par)
    response.raise_for_status()

    data = response.json()

    my_sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])

    my_sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])

    MY_POS = (my_sunrise, my_sunset)

    time_now = dt.datetime.now().hour

    if time_now >= my_sunset or time_now <= sunrise:
        return True


""" Send email"""

while True:

    if get_iss_location and sunrise:

        my_email = "mooalsyrian@gmail.com"
        my_password = "zpxuqldonobbkuwh"

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mohamedalboshey89@yahoo.com",
            msg="Subject:Hello\n\n Check the sunrise",
        )

    time.sleep(60)
