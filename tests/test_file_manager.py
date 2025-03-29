# -*- coding: utf-8 -*-
#   @Proyect:            Personal
#   @Author:             Adrian Epifanio
#   @File:               test_file_manager.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-03-29 08:13:50
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-03-29 09:12:42
#   @Description:        Tests for modules/files/file_manager.py


from modules.files.file_manager import FileManager

import pytest

def test_file_exist():
	assert(FileManager.file_exist(f_name='tests/tmp/sample.txt') == True)
	assert(FileManager.file_exist(f_name='tests/tmp/NonExistingFile.txt') == False)

def test_create_file():
	FileManager.create_file(f_name='tmp_file', content='Lorem Ipsum\nIpsumLorem', path='tests/tmp/', f_extension='.py')
	assert(FileManager.file_exist(f_name='tests/tmp/tmp_file.py') == True)
	assert('Error while creating \'tmp_file\'' in FileManager.create_file(f_name='tmp_file', path='tests/NonExistingPath/'))

def test_move_file():
	assert(FileManager.move_file(file_path='tests/tmp/sample.txt', destination_path='tests/sample.txt') == "File moved from 'tests/tmp/sample.txt' to 'tests/sample.txt'.")
	assert(FileManager.move_file(file_path='tests/tmp/sample.txt', destination_path='tests/sample.txt') == "Error: The file 'tests/tmp/sample.txt' does not exist.")
	assert(FileManager.move_file(file_path='tests/sample.txt', destination_path='tests/tmp/sample.txt') == "File moved from 'tests/sample.txt' to 'tests/tmp/sample.txt'.")
	assert('Error: ' in FileManager.move_file(file_path='tests/NonExistingPath/sample.txt', destination_path='tests/sample.txt'))

def test_copy_file():
	assert(FileManager.copy_file(source_file='tests/tmp/sample.txt', destination='tests/') == 'tests/sample.txt')
	FileManager.delete_file(file_path='tests/sample.txt')
	assert(FileManager.copy_file(source_file='tests/NonExistingPath/sample.txt', destination='tests/') == "Error, file 'tests/NonExistingPath/sample.txt' does not exist.")
	assert(FileManager.copy_file(source_file='tests/tmp/sample.txt', destination='tests/NonExistingPath/') == "Error, dir 'tests/NonExistingPath/' does not exist.")

def test_read_file():
	assert(FileManager.read_file(file_path='tests/tmp/tmp_file.py') == 'Lorem Ipsum\nIpsumLorem')
	assert(FileManager.read_file(file_path='tests/tmp/NonExistingFile') == "Error 404, 'tests/tmp/NonExistingFile' not found.")

def test_read_lines():
	assert(FileManager.read_lines(file_path='tests/tmp/tmp_file.py') == ['Lorem Ipsum', 'IpsumLorem'])
	assert(FileManager.read_lines(file_path='tests/tmp/NonExistingFile') == "Error 404, 'tests/tmp/NonExistingFile' not found.")

def test_add_line_to_file():
	FileManager.add_line_to_file(file_path='tests/tmp/tmp_file.py', line='NEW LINE')
	assert(FileManager.read_lines(file_path='tests/tmp/tmp_file.py') == ['Lorem Ipsum', 'IpsumLorem', 'NEW LINE'])
	# Delete tmp file
	FileManager.delete_file(file_path='tests/tmp/tmp_file.py')