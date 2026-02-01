# Michael Audi - CIS161 Extra Credit Assignment - Historical Ice Cream Prices

import datetime as dt
import csv

def load_prices(path="ice_cream_prices.csv"):
	'''
	This function takes a path to a csv containing a 2 column table of dates and prices as an argument and returns a dictionary of dates and prices.
	'''
	dictout = {}
	with open(path,'r',newline='') as table:
		for row in csv.DictReader(table):
			dictout.update({dt.date.fromisoformat(row["date"]): float(row["price"])})
	return dictout

def get_prices(month:int,year:int,path="ice_cream_prices.csv"):
	'''
	This function takes a month and year as arguments and returns the price of ice cream on that date.
	'''
	prices = load_prices(path)
	return prices[dt.date(year,month,1)]
