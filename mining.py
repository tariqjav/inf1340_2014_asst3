#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import csv
import datetime


stock_data = []
monthly_averages = []
total_sales = {}
total_volume = {}


def read_stock_data(stock_name, stock_file_name):
    #Telling python to read from the stock file
    with open(stock_file_name) as file_handle:
        file_contents = file_handle.read()
        # Storing the entire contents of the json file into a list variable
        stock_data = json.loads(file_contents)
        #Telling python to iterate through each dictionary in the data
        for element in stock_data:
            #Telling python to get the date and strip it as month/year
            date_entry = element.get("Date")
            parse_date = datetime.datetime.strptime(date_entry,"%Y-%m-%d")
            stock_date = datetime.datetime.strftime(parse_date,"%m-%Y")

            #Telling python to get the volume and the closing price
            #volume =[]
            #closing_price=[]
            #volume = element.get("Volume")
            #closing_price = element.get("Close")

            #Telling python to append the month/year into our total_sales dictionary as the key
            if stock_date in total_volume:
                stock_date = element.get("Date")
            else:
                total_volume[stock_date] = []




            #Telling python to get the stock volume
            #stock_volume = []
            #stock_volume = element.get("Volume")
            #stock_closing_price = []
            #stock_closing_price = element.get("Close")



            #Telling python to append the month/year into our total_volume dictionary as the key

                #else:
                    #total_volume[stock_date] = " "


            #stock_closing_price = element.get("Close")

        return print(total_volume)


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()
        # Storing the entire contents of the json file into a list variable
        stock_data = json.loads(file_contents)
    return stock_data

read_stock_data("GOOG","data/GOOG.json")