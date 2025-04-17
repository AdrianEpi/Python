# -*- coding: utf-8 -*-
#   @Proyect:            Personal
#   @Author:             Adrian Epifanio
#   @File:               csv_manager.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-04-17 09:40:42
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-04-17 10:04:30
#   @Description:        This file describes a csv manager. Contains all 
#                        the necessary methods to work with csv, create
#                        csv, read and transform it to other formats.

import pandas as pd
import os

class CsvManager:
	"""
	This class describes a csv manager.
	"""

	@staticmethod
	def csv_to_df(path: str, delimiter = None) -> pd.DataFrame:
		"""
		Transform a .csv file into a pandas dataframe.
		
		:param      path:       The path
		:type       path:       str
		:param      delimiter:  The file delimiter, such as , ; tab...
		:type       delimiter:  str
		
		:returns:   The pandas dataframe with the .csv data.
		:rtype:     Panda DataFrame
		"""
		return pd.read_csv(path, delimiter=delimiter)


	@staticmethod
	def csvs_from_dir_to_df_dict(path: str, delimiter = None) -> dict:
		"""
		Generates a dict of dataframes, where each key is the name of each .csv
		file found in a path and the value is a DataFrame with the data from
		that csv.
		
		:param      path:       The path
		:type       path:       str
		:param      delimiter:  The delimiter
		:type       delimiter:  str
		
		:returns:   A dictionary where the key is the file name and the value is
					the DataFrame.
		:rtype:     dict
		"""
		dataframes_dict = {}
		for file_name in os.listdir(path):
			if file_name.endswith('.csv'):
				file_path = os.path.join(path, file_name)
				df_name = file_name.replace('.csv', '')
				dataframes_dict[df_name] = pd.read_csv(file_path, delimiter=delimiter)

		return dataframes_dict


	@staticmethod
	def csv_to_dict(path: str, orient = 'list') -> dict:
		"""
		Transform a .csv file into a dict, where the key is the name of the
		column, and the value is an array of the elements in the column.
		
		:param      path:    The path
		:type       path:    str
		:param      orient:  The orient
		:type       orient:  str
		
		:returns:   Dictionary with the .csv data.
		:rtype:     dict
		"""
		return CsvManager.csv_to_df(path).to_dict(orient = orient)


	@staticmethod
	def df_to_csv(path: str, df: pd.DataFrame, sep = ';', header = True):
		"""
		Generates a .csv file with the data from the dataframe
		
		:param      path:    The f name
		:type       path:    str
		:param      df:      The dataframe
		:type       df:      pd.DataFrame
		:param      sep:     The separator
		:type       sep:     str
		:param      header:  The header
		:type       header:  bool
		"""
		df.to_csv(path, index=False, encoding = 'utf-8-sig', sep = sep, header = header)



	@staticmethod
	def data_to_csv(path: str, rows: list, columns: list):
		"""
		Generates a .csv file with the data in the rows and the columns as the
		header.
		
		:param      path:     The f name
		:type       path:     str
		:param      rows:     The rows
		:type       rows:     list
		:param      columns:  The columns
		:type       columns:  list
		"""
		CsvManager.df_to_csv(path = path, df = pd.DataFrame(rows, columns = columns), header = columns)