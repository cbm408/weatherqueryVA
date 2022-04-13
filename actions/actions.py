# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from actions.WeatherApis import get_weather_by_day
from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)


class WeatherForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "weather_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["date_time", "address"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        address = tracker.get_slot('address')
        date_time = tracker.get_slot('date_time')

        date_time_number = text_date_to_number_date(date_time)

        if isinstance(date_time_number, str):  # parse date_time failed
            dispatcher.utter_message("Currently does not support querying the weather of {}".format([address, date_time_number]))
        else:
            weather_data = get_weather_by_day(address, date_time_number)
            print(weather_data)
            print(date_time_number)
            
            dispatcher.utter_message(weather_data)
        return []


def text_date_to_number_date(text_date):
    L_week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if text_date == "now":
        return 0
    
    elif text_date == "today":
        return 1
    
    elif text_date == "tomorrow":
        return 2
    
    elif text_date == "the day after tomorrow" or text_date == "day after tomorrow":
        return 3

    elif text_date == ("next week"):
        return 4
    
    elif text_date in L_week_days:
        return L_week_days.index(text_date)+5
    
    else:
        # follow APIs are not supported by weather API provider freely
        return text_date

