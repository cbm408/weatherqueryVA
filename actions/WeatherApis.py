# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 02:37:32 2022

@author: 77469
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:40:07 2022

@author: 77469
"""

from bs4 import BeautifulSoup as bs
import requests
import argparse
from datetime import datetime
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.findAll("div")[0].attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result
    
def get_weather_by_day(address, number):
    try:
        URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
        # parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
        # parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
        #                                     Default is your current location determined by your IP Address""", default="")
        # # parse arguments
        # args = parser.parse_args()
        # region = args.region
        # print(region)
        # URL += region
        URL += ' ' + address
        # get data
        data = get_weather_data(URL)
        # print (data)
        # print("Weather for:", data["region"])
        # print("Now:", data["dayhour"])
        # print(f"Temperature now: {data['temp_now']}°C")
        # print("Description:", data['weather_now'])
        # print("Precipitation:", data["precipitation"])
        # print("Humidity:", data["humidity"])
        # print("Wind:", data["wind"])
        # print("Next days:")
        # for dayweather in data["next_days"]:
        #     print("="*40, dayweather["name"], "="*40)
        #     print("Description:", dayweather["weather"])
        #     print(f"Max temperature: {dayweather['max_temp']}°C")
        #     print(f"Min temperature: {dayweather['min_temp']}°C")
        if number == 0:
            return 'The weather in ' + address + ' at ' + data["dayhour"] + ' is ' + data['weather_now'].lower() + ', the temperature now is ' + data['temp_now'] + '°C, ' + 'precipitation is ' + data["precipitation"] + ', humidity is ' + data["humidity"] + ' and the wind speed is ' + data["wind"] + '.'
        if number == 1:
            return "Today's weather " + "in " + address + " is " + data["next_days"][0]["weather"].lower() + ", the highest temperature is " + data["next_days"][0]['max_temp'] + '°C, and the lowest temperature is ' + data["next_days"][0]['min_temp'] + '°C.'
        if number == 2:
            return "There could be " + data["next_days"][1]["weather"].lower() + " tomorrow in " + address + ", the highest temperature is " + data["next_days"][1]['max_temp'] + '°C, and the lowest temperature is ' + data["next_days"][1]['min_temp'] + '°C.'
        if number == 3:
            return "Expect partly " + data["next_days"][2]["weather"].lower() + ", the highest temperature is " + data["next_days"][2]['max_temp'] + '°C, and the lowest temperature is ' + data["next_days"][2]['min_temp'] + '°C.'
        if number == 4:
            text_next_week = "The next week's weather in " + address + " is: \n" 
            for dayweather in data["next_days"][1:]:
                text_next_week += 'On ' + dayweather["name"] + ", it will be like " + dayweather["weather"].lower() + ", the highest temperature is " + dayweather['max_temp'] + '°C, and the lowest temperature is ' + dayweather['min_temp'] + '°C. \n'
            return text_next_week
        if number in [5, 6, 7, 8, 9, 10, 11]:
            L = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day = datetime.today().weekday()
            print(day)
            if number - 5 == day:
                day = 7
            else:
                if number - 5 > day:
                    day = number - 5 - day
                else:
                    day = 7 - day + number - 5
            print(day)
            return "Looks like " + data["next_days"][day]["weather"].lower() + " on " + L[number-5] + " in " + address + ", the highest temperature is " + data["next_days"][day]['max_temp'] + '°C, and the lowest temperature is ' + data["next_days"][day]['min_temp'] + '°C.'
    except:
        return 'The weather query method is not yet supported'
if __name__ == "__main__":
    text = get_weather_by_day('Ottawa', 11)
    print(text)