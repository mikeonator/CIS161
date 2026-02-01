# Michael Audi - CIS161 Extra Credit Assignment - Historical Ice Cream Prices

import datetime as dt
import csv

def load_prices(path="ice_cream_prices.csv"):
	dictout = {}
	with open(path,'r',newline='') as table:
		for row in csv.DictReader(table):
			dictout.update({dt.date.fromisoformat(row["date"]): float(row["price"])})
	return dictout

def get_prices(month:int,year:int,path="ice_cream_prices.csv"):
	prices = load_prices(path)
	return prices[dt.date(year,month,1)]
