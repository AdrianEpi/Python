# -*- coding: utf-8 -*-
#   @Proyect:            Python Modules
#   @Author:             Adrian Epifanio
#   @File:               error_handler.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-03-28 17:08:45
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-03-29 09:46:13
#   @Description:        This file describes an ErrorHandler


import traceback
from datetime import datetime

class ErrorHandler:
	"""
	This class describes an error handler.
	"""
	error_str = ''

	@classmethod
	def log_error(cls, error_message, exception: Exception):
		"""
		Logs an error.
		
		:param      cls:            The cls
		:type       cls:            ErrorHandler
		:param      error_message:  The error message
		:type       error_message:  str / None
		:param      exception:      The exception
		:type       exception:      Exception
		"""
		if error_message != None and error_message != '':
			error_type = type(exception).__name__
			cls.error_str += f'\n\n{datetime.now()}: {error_message} - {error_type}\n'
			cls.error_str += f'{traceback.format_exc()}\n'


	@classmethod
	def log_error_no_exception(cls, error_message: str):
		"""
		Logs an error that did not cause an exception.

		:param      cls:            The cls
		:type       cls:            ErrorHandler
		:param      error_message:  The error message
		:type       error_message:  str
		"""
		cls.error_str += f'{datetime.now()}: {error_message}\n'
		cls.error_str += f'{traceback.format_exc()}\n'


	@classmethod
	def save_errors_to_file(cls, file_path: str):
		"""
		Saves an errors to file.
		
		:param      cls:        The cls
		:type       cls:        ErrorHandler
		:param      file_path:  The file path
		:type       file_path:  str
		"""
		if not cls.error_str:
			return
		timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
		full_path = f'{file_path}/error_log_{timestamp}.txt'
		with open(full_path, 'w') as file:
			file.write(cls.error_str)
		cls.error_str = ''


	@classmethod
	def print_errors(cls):
		"""
		Prints errors in the terminal.

		:param      cls:  The cls
		:type       cls:  ErrorHandler
		"""
		print(cls.error_str)


	@classmethod
	def to_s(cls) -> str:
		"""
		Returns a string with the error.

		:param      cls:  The cls
		:type       cls:  ErrorHandler

		:returns:   String representation of the error.
		:rtype:     str
		"""
		return cls.error_str


	@classmethod
	def reset(cls):
		"""
		Reset the error handler to empty the log.

		:param      cls:  The cls
		:type       cls:  ErrorHandler
		"""
		cls.error_str = ''



# Example
# try:
#     10 / 0
# except Exception as e:
#     ErrorHandler.log_error("Error en la división", e)

# file_path = os.getcwd() 
# ErrorHandler.save_errors_to_file(file_path)