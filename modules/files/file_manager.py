# -*- coding: utf-8 -*-
#   @Proyect:            Personal
#   @Author:             Adrian Epifanio
#   @File:               file_manager.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-03-29 08:04:19
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-03-29 09:12:34
#   @Description:        This file describes a file manager. Contains all 
#                        the necessary methods to work with files and directories.


import os
import shutil


class FileManager:
	"""
	This class describes a file manager, it cotains all the static methods
	needed to work with files, folders and directories.
	"""


	@staticmethod
	def file_exist(f_name: str) -> bool:
		"""
		Checks if a file exists
		
		:param      f_name:  The file name
		:type       f_name:  str
		
		:returns:   True if the file exists, false otherwise
		:rtype:     bool
		"""
		return os.path.isfile(f_name)


	@staticmethod
	def create_file(f_name: str, content = '', path = '', f_extension = ''):
		"""
		Creates a file.
		
		:param      f_name:       The file name
		:type       f_name:       str
		:param      content:      The file content
		:type       content:      str
		:param      path:         The path
		:type       path:         str
		:param      f_extension:  The file extension
		:type       f_extension:  str
		"""
		f = path + f_name + f_extension
		try:
			with open(f, 'w') as file:
				file.write(content)
		except Exception as e:
			return f"Error while creating '{f_name}': {e}"

	@staticmethod
	def delete_file(file_path: str):
		"""
		Deletes a file if it exists

		:param      file_path:  The file path
		:type       file_path:  str
		"""
		if os.path.isfile(file_path):
			os.remove(file_path)


	@staticmethod
	def move_file(file_path: str, destination_path: str) -> str:
		"""
		Moves a file to another dir

		:param      file_path:         The file path
		:type       file_path:         str
		:param      destination_path:  The destination path
		:type       destination_path:  str

		:returns:   String with the status.
		:rtype:     str
		"""
		try:
			os.rename(file_path, destination_path)
			return f"File moved from '{file_path}' to '{destination_path}'."
		except FileNotFoundError:
			return f"Error: The file '{file_path}' does not exist."
		except PermissionError:
			return f"Error: Permission denied for moving '{file_path}' to '{destination_path}'."
		except Exception as e:
			return f"Error: {e}"


	@staticmethod
	def copy_file(source_file: str, destination: str) -> str:
		"""
		Copy a file into the new destination
		
		:param      source_file:        The source file
		:type       source_file:        str
		:param      destination:        The destination
		:type       destination:        str
		
		:returns:   New path with the file
		:rtype:     str
		"""
		try:
			file_name = os.path.basename(source_file)
			destination_file = os.path.join(destination, file_name)
			shutil.copy(source_file, destination_file)
			return destination_file
		except Exception as e:
			if not os.path.exists(source_file):
				return f"Error, file '{source_file}' does not exist."
			
			if not os.path.exists(destination):
				return f"Error, dir '{destination}' does not exist."
			return f"Error: {e}"


	@staticmethod
	def read_file(file_path: str) -> str:
		"""
		Reads a file.

		:param      file_path:  The file name
		:type       file_path:  str

		:returns:   Data readed from the file
		:rtype:     str
		"""
		try:
			with open(file_path, 'r', encoding='utf-8') as file:
				content = file.read()
			return content
		except FileNotFoundError:
			return f"Error 404, '{file_path}' not found."
		except Exception as e:
			return f"Unexpected error while attempting to read file '{file_path}', with error code: {e}"


	@staticmethod
	def read_lines(file_path: str) -> list:
		"""
		Reads the lines in a file and creates a list from them.
		
		:param      file_path:  The file name
		:type       file_path:  str
		
		:returns:   List with one readed line per item in the list
		:rtype:     list
		"""
		try:
			with open(file_path, 'r', encoding='utf-8') as file:
				content = [line.strip() for line in file.readlines() if line.strip()]
			return content
		except FileNotFoundError:
			return f"Error 404, '{file_path}' not found."
		except Exception as e:
			return f"Unexpected error while attempting to read lines in file '{file_path}', with error code: {e}"


	@staticmethod
	def add_line_to_file(file_path: str, line: str):
		"""
		Adds a line to file.

		:param      file_path:  The file path
		:type       file_path:  str
		:param      line:       The line
		:type       line:       str
		"""
		try:
			with open(file_path, 'a', encoding='utf-8') as file:
				file.write('\n' + line)
		except Exception as e:
			return f"Error while attepmting to add line to file.\nFile Path: '{file_path}'\nLine: {line}\nError: {e}"