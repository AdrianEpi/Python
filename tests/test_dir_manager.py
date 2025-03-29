# -*- coding: utf-8 -*-
#   @Proyect:            Personal
#   @Author:             Adrian Epifanio
#   @File:               test_dir_manager.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-03-29 09:37:35
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-03-29 10:27:16
#   @Description:        Test modules/filesystem/dir_manager.py


from modules.filesystem.dir_manager import DirManager

import pytest

def test_list_dirs():
	assert('tmp' in DirManager.list_dirs(path='tests'))
	assert(DirManager.list_dirs(path='NonExistingPath') == "Error: The directory 'NonExistingPath' does not exist.")

def test_list_files():
	tmp_list = ['sample.txt']
	assert(tmp_list == DirManager.list_files(path='tests/tmp/'))
	assert([] == DirManager.list_files(path='tests/tmp/', extension='.py'))
	assert('Error: The directory \'tests/NonExistingPath/\' does not exist.' == DirManager.list_files(path='tests/NonExistingPath/'))

def test_list_all_files_recursive():
	tmp_list = ['sample.txt']
	assert(tmp_list == DirManager.list_all_files_recursive(path='tests/tmp/'))
	assert([] == DirManager.list_all_files_recursive(path='tests/tmp/', extension='.py'))

def test_dir_exist():
	assert(DirManager.dir_exist(path='tests') == True)

def test_create_dir():
	DirManager.create_dir(path='tests/tmp/new_dir')
	assert(DirManager.dir_exist(path='tests/tmp/new_dir') == True)
	assert('Error while creating dir' in DirManager.create_dir(path='tests/tmp//'))

def test_get_current_dir():
	d = DirManager.get_current_dir()
	assert(DirManager.dir_exist(d))

def test_create_dir_hierarchy():
	a = ['a', 'b', 'c']
	b = [['d', 'e'], 'x', 'y']
	DirManager.create_dir_hierarchy(data=a, path='tests/tmp/new_dir')
	DirManager.create_dir_hierarchy(data=b, path='tests/tmp/new_dir')
	for i in a:
		assert(DirManager.dir_exist('tests/tmp/new_dir/' + i) == True)
	for i in b[0]:
		assert(DirManager.dir_exist('tests/tmp/new_dir/' + i + '/x') == True)
		assert(DirManager.dir_exist('tests/tmp/new_dir/' + i + '/y') == True)

def test_delete_dir():
	DirManager.delete_dir(path='tests/tmp/new_dir')
	assert(DirManager.dir_exist(path='tests/tmp/new_dir') == False)