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

def compute_avg(data, list_close):
    '''
    :param data: month of the year
    :param list: list of tuple of (closing and volume)
    :return: average
    '''
    sum = 0
    vol_total = 0
    for key in list_close:
        sum += key[0] * key[1]
        vol_total += key[1]

    return sum / vol_total


def read_stock_data(stock_name, stock_file_name):
    '''
    read_stock_data
    :param stock_name: The name of the stock
    :param stock_file_name: The name of the file holding the stock values.
    :return:

    '''

    # Check Types of arguments passed in
    if not type(stock_name) is str:
        raise TypeError("Type Error: Please Pass in stock name in string")


    if not type(stock_file_name) is str:
        raise TypeError("Type Error: Please Pass in stock file name in string")



    best_six = []
    worst_six = []
    #Telling python to read from the stock file
    with open(stock_file_name) as file_handle:
        file_contents = file_handle.read()
        # Storing the entire contents of the json file into a list variable
        stock_data = json.loads(file_contents)
        #Telling python to iterate through each dictionary in the data
        dict_elem = {}
        prev_date = 0
        for element in stock_data:
            #Telling python to get the date and strip it as month/year
            date_entry = element.get("Date")
            parse_date = datetime.datetime.strptime(date_entry,"%Y-%m-%d")
            stock_date = datetime.datetime.strftime(parse_date,"%m-%Y")

            #Telling python to get the volume and the closing price

            volume = element.get("Volume")
            closing_price = element.get("Close")

            # compare and see if the date of the element just read is the same as the previous
            # element date or not, if not, we can compute the average now as we have read the data
            # for all the month.

            # TO DO: Once comparison is done, we can compare it with TOP 6 months that we have so
            # far, if its better we update the TOP 6 months to include this one and drop the 7th one

            # TO DO: We also have to do the comparison to TOP worst 6 months and include this month
            # in those month is the avg is very low

            if stock_date == prev_date:
                dict_elem[stock_date].append((closing_price, volume))
            else:
                if prev_date in dict_elem:
                    avg = compute_avg(prev_date, dict_elem[prev_date])
                    # Creating a tuple which will have the stock date and average
                    # As long as the length is less than 6, append the date and average tuple into the list
                    # For every 7th element to add from the monthly average list, compare with six elements
                    # inside best six

                    if len(best_six) < 6:
                        best_six.append((avg, stock_date))
                    else:
                        #for the six tuples already in the list:
                        top_avg = sorted(best_six)
                        if avg > top_avg[0][0]:
                            best_six.remove(top_avg[0])
                            best_six.append(((avg, stock_date)))

                    if len(worst_six) < 6:
                        worst_six.append((avg, stock_date))
                    else:
                        #for the six tuples already in the list:
                        low_avg = sorted(worst_six)
                        if avg < worst_six[5][0]:
                            worst_six.remove(low_avg[5])
                            worst_six.append(((avg, stock_date)))


                dict_elem[stock_date] = [(closing_price, volume)]

            # Keep what is previous date.
            prev_date = stock_date


    print(best_six)
    print(worst_six)

    return


def read_json_from_file(file_name):
    '''

    :param file_name:
    :return:
    '''
    with open(file_name) as file_handle:
        file_contents = file_handle.read()
        # Storing the entire contents of the json file into a list variable
        stock_data = json.loads(file_contents)
    return stock_data

read_stock_data("GOOG", "data/GOOG.json")