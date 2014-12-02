#!/usr/bin/env python3

""" This will test the mining program """

__author__ = 'Nazanin Tehrani & Javeria Tariq'

__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import mining
from mining import *
import pytest


def test_basic_GOOG():
    '''
    # Test for GOOG
    :return: Does not return anything
    '''


    # The six worst month has been updated as 08-2004 is among lowest months but was not included in the initial test
    # data, we understand that data for this month is not complete as only half of the month are in the JSON, but we
    # still included it in the final results as it has one of the lowest avgs.

    # All numbers are rounded with 2 decimals.

    # To ensure all lists have equivalent members, they are all sorted based on the avg, in descending (in case of best)
    # and ascending (in case of worst)

    # We were confused what format to use for the dates in the tuple, we stick to what we have in the JSON, which is
    # the delimiter of '-' between month and year.


    read_stock_data("GOOG", "data/GOOG.json")
    assert six_best_months()  == sorted([(693.76, '12-2007'), (676.55,'11-2007'), (637.38, '10-2007'), (599.42, '01-2008'), (576.29, '05-2008'), (555.34, '06-2008')], reverse=True)

    assert six_worst_months()  == sorted([(104.66, '08-2004'), (116.38, '09-2004'), (164.52, '10-2004'), (177.09, '11-2004'), (181.01, '12-2004'), (181.18, '03-2005')])


def test_basic_TSE():
    '''
    # Test for TSE-SO
    :return: Does not return anything
    '''

    read_stock_data("TSE-SO", "data/TSE-SO.json")
    assert six_best_months() == sorted([(20.98, '12-2007'), (20.89, '11-2007'), (19.96, '05-2013'), (19.94, '06-2013'), (19.65, '04-2013'), (19.11, '10-2007')], reverse=True)
    assert six_worst_months() == sorted([(1.74, '03-2009'), (2.08, '11-2008'), (2.25, '12-2008'), (2.41, '02-2009'), (2.75, '04-2009'), (3.14, '01-2009')])


def test_file_name_type():
    '''
    Test for corner cases when there is a problem with the input passed
    :return: Does not return anything
    '''

    # When file name passed are string but name is not defined
    with pytest.raises(IOError):
        read_stock_data("GOOG", "randomdatafile.json")


    # When stock name passed is not string
    with pytest.raises(TypeError):
        read_stock_data(1313232414, "data/GOOG.json")

    # When file name passed is not string
    with pytest.raises(TypeError):
        read_stock_data("TSE-SO", 313213)

    # When file does not exist
    with pytest.raises(IOError):
        read_stock_data("ABC", "data/ABC.json")

def test_compare_STD():
    '''
    Test for bonus: Standard Deviation Computation
    :return: Does not return anything
    '''

    read_stock_data("GOOG", "data/GOOG.json")
    assert compare_two_avg('2004-08-23', '2004-08-20') == 2

    with pytest.raises(TypeError):
        compare_two_avg(11, '2004-08-20')

    with pytest.raises(TypeError):
        compare_two_avg('2004-08-20', 12)

    with pytest.raises(ValueError):
        compare_two_avg('2016', '2016')
