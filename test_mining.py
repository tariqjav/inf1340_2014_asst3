#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import mining
from mining import *


def test_goog(best_six, worst_six):
    read_stock_data("GOOG", "data/GOOG.json")
    assert best_six == [(693.76, '12-2007'), (676.55,'11-2007'), (637.38, '10-2007'), (599.42, '01-2008'),
                                 (576.29, '05-2008'), (555.34, '06-2008')]
    assert worst_six == [(116.38, '09-2004'), (164.52, '10-2004'), (177.09, '11-2004'), (181.01, '12-2004'),
                                  (181.18, '03-2005'), (192.96, '01-2005')]


def test_tse_so(best_six, worst_six):
    read_stock_data("TSE-SO", "data/TSE-SO.json")
    assert best_six == [(17.99, '12-2004'), (20.81,'04-2007'), (18.33, '11-2008'), (19.42, '04-2009'),
                                 (21.76, '05-2013'), (17.8, '06-2009')]
    assert worst_six == [(6.45, '11-2004'), (9.44, '12-2007'), (11.31, '01-2008'), (4.09, '05-2013'),
                                  (10.48, '06-2013'), (1.89, '12-2009')]


def test_file_name_type(file_name):
    assert file_name == "data/TSE-SO.json"
    assert file_name == "data/GOOG.json"
    assert file_name == "data/fileABC.json"
    



