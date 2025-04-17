# -*- coding: utf-8 -*-
#   @Proyect:            Personal
#   @Author:             Adrian Epifanio
#   @File:               test_csv_manager.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-04-17 09:50:11
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-04-17 10:15:31
#   @Description:        Test modules/filesystem/csv_manager.py

from modules.filesystem.csv_manager import CsvManager

import pytest
import pandas as pd


def test_csv_to_df():
	assert(CsvManager.csv_to_df(path='tests/tmp_csv/sample.csv').empty == False)


def test_csvs_from_dir_to_df_dict():
	assert(len(CsvManager.csvs_from_dir_to_df_dict(path='tests/tmp_csv/')) == 2)

def test_csv_to_dict():
	assert(len(CsvManager.csv_to_dict(path='tests/tmp_csv/sample.csv')) == 3)

def test_df_to_csv():
	df = pd.DataFrame({'A': [1]})
	CsvManager.df_to_csv(path='tests/tmp_csv/sample_2.csv', df=df)
	assert(len(CsvManager.csv_to_dict(path='tests/tmp_csv/sample_2.csv')) == 1)
	df2 = pd.DataFrame(CsvManager.csv_to_dict(path='tests/tmp_csv/sample.csv'))
	CsvManager.df_to_csv(path='tests/tmp_csv/sample_2.csv', df=df2, sep=',')
	assert(len(CsvManager.csv_to_dict(path='tests/tmp_csv/sample_2.csv')) == 3)

def test_data_to_csv():
	rows = ['A']
	columns = [1]
	CsvManager.data_to_csv(path='tests/tmp_csv/sample_2.csv', rows=rows, columns=columns)
	assert(len(CsvManager.csv_to_dict(path='tests/tmp_csv/sample_2.csv')) == 1)
	df2 = pd.DataFrame(CsvManager.csv_to_dict(path='tests/tmp_csv/sample.csv'))
	CsvManager.df_to_csv(path='tests/tmp_csv/sample_2.csv', df=df2, sep=',')
	assert(len(CsvManager.csv_to_dict(path='tests/tmp_csv/sample_2.csv')) == 3)
