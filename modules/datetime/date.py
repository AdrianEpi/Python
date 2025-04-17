# -*- coding: utf-8 -*-
#   @Proyect:            Python Modules
#   @Author:             Adrian Epifanio
#   @File:               date.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-03-28 17:08:06
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-04-17 09:39:13
#   @Description:        This file describes a Date class


from datetime import datetime
from modules.errors.error_handler import ErrorHandler

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]

MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
	"""
	This class describes a date.
	"""

	def __init__(self, day = None, month = None, year = None):
		"""
		Constructs a new instance.
		
		:param      day:    The day
		:type       day:    str / int
		:param      month:  The month
		:type       month:  str / int
		:param      year:   The year
		:type       year:   str / int
		"""
		self.set_current_date()
		if (year and month and day):
			self.set_year(year)
			self.set_month(month)
			self.set_day(day)
		# else:
		# 	self.set_current_date()


	def set_current_date(self):
		"""
		Sets the date to the current date.
		"""
		self.year = datetime.now().year
		self.month = datetime.now().month
		self.day = datetime.now().day


	def set_year(self, year):
		"""
		Sets the year.

		:param      year:  The year
		:type       year:  int or str
		"""
		if type(year) == str:
			try:
				self.year = int(year)
			except Exception as e:
				error = f'Error, year is not a number.'
				ErrorHandler.log_error(error, e)
		elif type(year) != int:
			error = f'Error, year is not an int or string.' 
			ErrorHandler.log_error_no_exception(error)
		else:
			self.year = year


	def set_month(self, month):
		"""
		Sets the month.

		:param      month:  The month
		:type       month:  int or str
		"""
		if type(month) == str:
			if month.isdigit():
				self.month = int(month)
			elif month.capitalize() in MONTHS:
				self.month = MONTHS.index(month.capitalize())
			else:
				error = f'Error, month is not a number or is not written propertly.'
				ErrorHandler.log_error_no_exception(error)
		elif type(month) == int:
			if month < 1 or month > 12:
				error = f'Error, month out of range.'
				ErrorHandler.log_error_no_exception(error)
			else:
				self.month = month
		else:
			error = f'Error, month is not an int or string.'
			ErrorHandler.log_error_no_exception(error)


	def set_day(self, day):
		"""
		Sets the day.

		:param      day:  The new value
		:type       day:  int or str
		"""

		if type(day) == str:
			try:
				self.day = int(day)
			except Exception as e:
				error = f'Error, day is not a number'
				ErrorHandler.log_error(error, e)
		elif type(day) == int:
			if day < 0 or day > MONTH_DAYS[self.month - 1]:
				error = f'Error, day value is out of range.'
				ErrorHandler.log_error_no_exception(error)
			else:
				self.day = day
		else:
			error = f'Error, day is not an int or string.'
			ErrorHandler.log_error_no_exception(error)
		

	def get_yymmdd(self) -> str:
		"""
		Gets the yymmdd. (YYYY-MM-DD)
	 
		:returns:   The yymmdd.
		:rtype:     str
		""" 
		day = str(self.day)
		month = str(self.month)
		if len(day) < 2:
			day = '0' + day 
		if len(month) < 2:
			month = '0' + month 
		return f'{str(self.year)}-{month}-{day}'

	
	def get_yymm(self) -> str:
		"""
		Gets the yymm. (YYYY-MM)
	 
		:returns:   The yymm.
		:rtype:     str
		""" 
		return self.get_yymmdd()[:7]

	
	def get_year_month(self) -> str:
		"""
		Gets the year month. (2024 December)
	 
		:returns:   The year month.
		:rtype:     str
		""" 
		return f'{str(self.year)} {MONTHS[self.month - 1]}'

	
	def get_month_year(self) -> str:
		"""
		Gets the month year. (December 2024)
	 
		:returns:   The month year.
		:rtype:     str
		""" 
		return f'{MONTHS[self.month - 1]} {str(self.year)}'

	
	def get_day_month(self) -> str:
		"""
		Gets the day month. (5 December)
	 
		:returns:   The day month.
		:rtype:     str
		""" 
		return f'{str(self.day)} {MONTHS[self.month - 1]}'

	
	def get_month_day(self) -> str:
		"""
		Gets the month day. (December 5)
	 
		:returns:   The month day.
		:rtype:     str
		""" 
		return f'{MONTHS[self.month - 1]} {str(self.day)}'