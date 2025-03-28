# -*- coding: utf-8 -*-
#   @Proyect:            Personal
#   @Author:             Adrian Epifanio
#   @File:               test_date.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-03-28 17:10:18
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-03-28 17:24:09
#   @Description:        ...



from modules.datetime.date import Date
from modules.errors.error_handler import ErrorHandler

import pytest


current_date = Date() # Sets current date
date = Date(day=31, month=12, year=2024) # Sets date in numeric format
date2 = Date(day='5', month='9', year='1999') # Sets date in str format
date3 = Date(day=24, month='December', year=2024) # Sets date in mixed format

def test_set_current_date():
	date3.set_current_date()
	assert(current_date.day == date3.day)
	assert(current_date.month == date3.month)
	assert(current_date.year == date3.year)

def test_get_yymmdd():
	assert(date.get_yymmdd() == '2024-12-31')
	assert(date2.get_yymmdd() == '1999-09-05')

def test_get_yymm():
	assert(date.get_yymm() == '2024-12')
	assert(date2.get_yymm() == '1999-09')

def test_get_year_month():
	assert(date.get_year_month() == '2024 December')
	assert(date2.get_year_month() == '1999 September')

def test_get_month_year():
	assert(date.get_month_year() == 'December 2024')
	assert(date2.get_month_year() == 'September 1999')

def test_get_day_month():
	assert(date.get_day_month() == '31 December')
	assert(date2.get_day_month() == '5 September')

def test_get_month_day():
	assert(date.get_month_day() == 'December 31')	
	assert(date2.get_month_day() == 'September 5')

def test_set_year_errors():
	ErrorHandler.reset()
	date2.set_year('AAA')
	assert('Error, year is not a number.' in ErrorHandler.to_s())
	
	ErrorHandler.reset()
	date2.set_year(True)
	assert('Error, year is not an int or string.' in ErrorHandler.to_s())

def test_set_month_errors():
	ErrorHandler.reset()
	date2.set_month('Dycember')
	assert('Error, month is not a number or is not written propertly.' in ErrorHandler.to_s())
	
	ErrorHandler.reset()
	date2.set_month(True)
	assert('Error, month is not an int or string.' in ErrorHandler.to_s())

	ErrorHandler.reset()
	date2.set_month(20)
	assert('Error, month out of range.' in ErrorHandler.to_s())


def test_set_day_errors():
	ErrorHandler.reset()
	date2.set_day('aa')
	assert('Error, day is not a number' in ErrorHandler.to_s())
	
	ErrorHandler.reset()
	date2.set_day(True)
	assert('Error, day is not an int or string.' in ErrorHandler.to_s())

	ErrorHandler.reset()
	date2.set_day(40)
	assert('Error, day value is out of range.' in ErrorHandler.to_s())
