#!/usr/bin/env python3

""" This program will find out the monthly average of a stock over a period of time.
It will provide the user with the best six months and the worst six months of the particular stock. """

__author__ = 'Nazanin Tehrani & Javeria Tariq'

__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import csv
import datetime

best_6 = []
worst_6 = []
stock_data = []
avg_data = {}
dict_overall = {}

def compute_avg(data, list_close):
    """
    :param data: month of the year
    :param list_close: list of tuple of (closing and volume)
    :return: average
    """
    total = 0
    vol_total = 0
    for key in list_close:
        total += key[0] * key[1]
        vol_total += key[1]

    return round(total / vol_total,2)


def read_stock_data(stock_name, stock_file_name):
    """
    read_stock_data
    :param stock_name: The name of the stock
    :param stock_file_name: The name of the file holding the stock values
    :return:
    """

    avg_ = {}
    dict_all = {}
    best_six = []
    worst_six = []
    # Check Types of arguments passed in
    if not type(stock_name) is str:
        raise TypeError("Type Error: Please Pass stock name in string")

    if not type(stock_file_name) is str:
        raise TypeError("Type Error: Please Pass stock file name in string")


    # Create a list which will store the best six and worst six

    # Read from the stock file
    with open(stock_file_name) as file_handle:
        file_contents = file_handle.read()
        # Storing the entire contents of the json file into a list variable
        stock_data = json.loads(file_contents)
        #Iterate through each dictionary in the stock data from the json file
        dict_elem = {}
        prev_date = 0
        for element in stock_data:
            #Get the date and strip it as month/year
            date_entry = element.get("Date")
            parse_date = datetime.datetime.strptime(date_entry,"%Y-%m-%d")
            stock_date = datetime.datetime.strftime(parse_date,"%m-%Y")


            #Get the volume and the closing price
            volume = element.get("Volume")
            closing_price = element.get("Close")
            dict_all[date_entry] = round(closing_price,2)
            # Compare if the date of the element just read is the same as the previous date. Are they in the same month?
            # element date or not, if not, we can compute the average now as we have read the data
            # for all the month.
            if stock_date == prev_date:
                dict_elem[stock_date].append((closing_price, volume))
            else:
                if prev_date in dict_elem:
                    avg = compute_avg(prev_date, dict_elem[prev_date])
                    # Creating a tuple which will have the stock date and average
                    # As long as the length is less than 6, append the date and average tuple into the list
                    # For every 7th element to add from the monthly average list, compare with six elements
                    # If smaller than worst cases or larger than best cases then we need to insert it into
                    # corresponding array.
                    avg_[prev_date] = avg
                    if prev_date == 0:
                        best_six = []
                    if len(best_six) < 6:
                        best_six.append((avg, prev_date))
                    else:
                        #for the six tuples already in the list:
                        top_avg = sorted(best_six)
                        if avg > top_avg[0][0]:
                            best_six.remove(top_avg[0])
                            best_six.append((avg, prev_date))

                    if len(worst_six) < 6:
                        worst_six.append((avg, prev_date))
                    else:
                        #for the six tuples already in the list:
                        low_avg = sorted(worst_six)
                        if avg < low_avg[5][0]:
                            worst_six.remove(low_avg[5])
                            worst_six.append((avg, prev_date))


                dict_elem[stock_date] = [(closing_price, volume)]

            # Keep what is previous date.
            prev_date = stock_date

    if prev_date in dict_elem:
                    avg = compute_avg(prev_date, dict_elem[prev_date])
                    # Creating a tuple which will have the stock date and average
                    # As long as the length is less than 6, append the date and average tuple into the list
                    # For every 7th element to add from the monthly average list, compare with six elements
                    # If smaller than worst cases or larger than best cases then we need to insert it into
                    # corresponding array.
                    avg_[prev_date] = avg
                    if prev_date == 0:
                        best_six = []
                    if len(best_six) < 6:
                        best_six.append((avg, prev_date))
                    else:
                        #for the six tuples already in the list:
                        top_avg = sorted(best_six)
                        if avg > top_avg[0][0]:
                            best_six.remove(top_avg[0])
                            best_six.append((avg, prev_date))

                    if len(worst_six) < 6:
                        worst_six.append((avg, prev_date))
                    else:
                        #for the six tuples already in the list:
                        low_avg = sorted(worst_six)
                        if avg < low_avg[5][0]:
                            worst_six.remove(low_avg[5])
                            worst_six.append((avg, prev_date))


    global best_6, worst_6, avg_data, dict_overall
    best_6 = best_six
    worst_6 = worst_six
    avg_data = avg_
    dict_overall = dict_all
    return


def compare_two_avg(date1, date2):
    '''

    :param date1: date1
    :param date2: date2
    :return: 1 if standard deviation of 1 is bigger; 2 otherwise
    '''

    # Check for data types and ensure date1 is string
    if not type(date1) is str:
        raise TypeError("Type Error: Please Pass date name in string")

    # Check for data types and ensure date2 is string
    if not type(date2) is str:
        raise TypeError("Type Error: Please Pass date name in string")

    # Check for date1 value and raise an error if it does not exists
    if date1 in dict_overall:
        num_1 = dict_overall[date1]
    else:
        raise ValueError("Value Error: Please Pass valid date string")

    # Check for date1 value and raise an error if it does not exists
    if date2 in dict_overall:
        num_2 = dict_overall[date2]
    else:
        raise ValueError("Value Error: Please Pass valid date string")


    # Compute Standard Deviation -
    parse_date = datetime.datetime.strptime(date1,"%Y-%m-%d")
    stock_date_1 = datetime.datetime.strftime(parse_date,"%m-%Y")

    std_num_1 = (num_1 - avg_data[stock_date_1]) * (num_1 - avg_data[stock_date_1])

    parse_date = datetime.datetime.strptime(date2,"%Y-%m-%d")
    stock_date_2 = datetime.datetime.strftime(parse_date,"%m-%Y")

    std_num_2 = (num_2 - avg_data[stock_date_2]) * (num_2 - avg_data[stock_date_2])

    if std_num_1 > stock_date_2:
        return 1
    else:
        return 2

def set_best(best_):
    '''

    :param best_: local best_ is used to set the value to global best_6 variable
    :return: does not return anything
    '''
    global best_6
    best_6 = best_
    print(best_6)


def set_worst(worst_):
    '''

    :param worst_: local worst_ is used to set the value to global worst_6 variable
    :return: does not return anything
    '''
    global worst_6
    worst_6 = worst_


def six_best_months():
    '''
    get function to return the value of global best_6 variable
    :return: best_6
    '''
    return sorted(best_6, reverse=True)

def six_worst_months():
    '''
    get function to return the value of global worst_6 variable
    :return: worst_6
    '''
    return sorted(worst_6)

def read_json_from_file(file_name):
    """
    :param file_name: the file to read from
    :return: contents inside the file
    """
    with open(file_name) as file_handle:
        file_contents = file_handle.read()
        # Storing the entire contents of the json file into a list variable
        stock_data = json.loads(file_contents)
    return stock_data



