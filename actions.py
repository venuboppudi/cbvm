from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import re
import pandas as pd


class Actionlocationverification(Action):
    def name(self):
        return 'action_verify_location'

    def run(self, dispatcher, tracker, domain):

        loc_service = ["ahmedabad", "bangalore", "chennai", "delhi", "hyderabad", "kolkata", "mumbai", "pune", "agra", "ajmer", "aligarh", "allahabad", "amravati", "amritsar",
                       "asansol", "aurangabad", "bareilly", "belgaum", "bhavnagar", "bhiwandi", "bhopal", "bhubaneswar", "bikaner", "bokaro steel city", "chandigarh", "coimbatore",
                       "cuttack", "dehradun", "dhanbad", "durg-bhilai nagar", "durgapur", "erode", "faridabad", "firozabad", "ghaziabad", "gorakhpur", "gulbarga", "guntur", "gurgaon",
                       "guwahati", "hubli-dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar", "jamshedpur", "jhansi", "jodhpur", "kannur", "kanpur", "kakinada",
                       "kochi", "kottayam", "kolhapur", "kollam", "kota", "kozhikode", "kurnool", "lucknow", "ludhiana", "madurai", "malappuram", "mathura", "goa", "mangalore", "meerut",
                                "moradabad", "mysore", "nagpur", "nanded", "nashik", "nellore", "noida", "palakkad", "patna", "pondicherry", "raipur", "rajkot", "rajahmundry", "ranchi", "rourkela",
                                "salem", "sangli", "siliguri", "solapur", "srinagar", "sultanpur", "surat", "thiruvananthapuram", "thrissur", "tiruchirappalli", "tirunelveli", "tiruppur", "ujjain",
                                "vijayapura", "vadodara", "varanasi", "vasai-virar city", "vijayawada", "visakhapatnam", "warangal", "gwalior"]
        loc = tracker.get_slot('location')
        if loc is not None:
            if loc.lower() in loc_service:
                return[SlotSet('location', loc)]
            else:
                dispatcher.utter_message(
                    "Sorry we do not have services for this location")
                return[SlotSet('location', None)]


class ActionCuisineverification(Action):
    def name(self):
        return 'action_verify_cuisine'
        # action_validate_cuisine'

    def run(self, dispatcher, tracker, domain):
        list_cuisine = ["chinese", "mexican", "american",
                        "italian", "south indian", "north indian"]
        cuisine = tracker.get_slot('cuisine')
        if cuisine is not None:
            if cuisine.lower() in list_cuisine:
                return[SlotSet('cuisine', cuisine)]

            else:
                dispatcher.utter_message(
                    "Sorry we provide only chinese,mexican,american,italian,south indian,north indian")
                return[SlotSet('cuisine', None)]
        else:
            dispatcher.utter_message(
                "Sorry I could not understand the cuisine name you provided , please check typo errors")
            return[SlotSet('cuisine', None)]


class ActionBudgetverification(Action):
    def name(self):
        return 'action_verify_budget'

    def run(self, dispatcher, tracker, domain):
        cost_queried = tracker.get_slot('budget')
        if cost_queried == 'less than 300' or cost_queried == 'lesser than 300' or cost_queried == '< 300'or ("cheap" in cost_queried):
            return[SlotSet('budget', 'low')]
        elif cost_queried == 'more than 700'or cost_queried == 'greater than 700' or cost_queried == '> 700' or ("costly" in cost_queried) or ("expensive" in cost_queried):
            return[SlotSet('budget', 'high')]
        else:
            # always return mid budget by default
            return[SlotSet('budget', 'mid')]


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": ""}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        budget = tracker.get_slot('budget')

        if budget == 'low':
            cost_to_filer_min = 0
            cost_to_filer_max = 300
        elif budget == 'mid':
            cost_to_filer_min = 301
            cost_to_filer_max = 700
        elif budget == 'high':
            cost_to_filer_min = 701
            cost_to_filer_max = 9999
        cols = ['restaurant name', 'restaurant address',
                'avg. budget for two', 'zomato rating']
        restaurant_df = pd.DataFrame(columns=cols)

        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'american': 1, 'chinese': 25, 'mexican': 73,
                         'italian': 55, 'north indian': 50, 'south indian': 85}
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 10)
        print(results)
        d = json.loads(results)
        response = ""
        for i in range(10):
            if d['results_found'] != 0:
                for restaurant in d['restaurants']:
                    curr_res = {'zomato rating': restaurant['restaurant']["user_rating"]["aggregate_rating"], 'restaurant name': restaurant['restaurant']['name'],
                                'restaurant address': restaurant['restaurant']['location']['address'], 'avg. budget for two': restaurant['restaurant']['average_cost_for_two']}
                    if (curr_res['avg. budget for two'] >= cost_to_filer_min) and (curr_res['avg. budget for two'] <= cost_to_filer_max):
                        restaurant_df.loc[len(restaurant_df)] = curr_res

        restaurant_df = restaurant_df.sort_values(
            ['zomato rating', 'avg. budget for two'], ascending=[False, True])

        restaurant_df = restaurant_df.head(10)
        restaurant_df = restaurant_df.reset_index(drop=True)
        restaurant_df.index = restaurant_df.index.map(str)

        if len(restaurant_df) != 0:
            for index, row in restaurant_df.iterrows():
                response = response + index + ". Found \"" + \
                    row['restaurant name'] + "\" in " + row['restaurant address'] + \
                    " has been rated " + row['zomato rating']+"\n"
        else:
            response = 'Found 0 restaurants in given price range'

        dispatcher.utter_message(response)
        return [SlotSet('budget', budget)]


class ActionEmailverify(Action):
    def name(self):
        return 'action_verify_email'

    def run(self, dispatcher, tracker, domain):
        email_check = tracker.get_slot('email')
        if email_check is not None:
            if re.search("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+.[a-zA-Z0-9_-]+)", email_check):
                dispatcher.utter_message(
                    "we have sent you a mail regarding the details to your mail id")
                return[SlotSet('email', email_check)]
            else:
                dispatcher.utter_message("Sorry this is not a valid email")
                return[SlotSet('email', None)]
        else:
            dispatcher.utter_message("Please provide your email id again")
            return[SlotSet('email', None)]

# not worked on sending mail to the person just print the statement " we have sent the mail regarding the details of the restaurant search to your mail id"
