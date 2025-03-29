# -*- coding: utf-8 -*-
#   @Proyect:            Python Modules
#   @Author:             Adrian Epifanio
#   @File:               dir_manager.py
#   @Author:             Adrian Epifanio
#   @Date:               2025-03-29 09:37:27
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2025-03-29 09:45:45
#   @Description:        This file describes a directory manager. Contains all
#                        the necessary methods to work with directories in the OS.


class DirManager:

	@staticmethod
	def list_dirs(path: str) -> list:
		"""
		List all the directories in the given path

		:param      path:  The path
		:type       path:  str

		:returns:   List with the directories names
		:rtype:     list
		"""
		try:
			return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
		except FileNotFoundError:
			return f"Error: The directory '{path}' does not exist."
		except PermissionError:
			return f"Error: Permission denied for accessing '{path}'."


	@staticmethod
	def list_files(path: str, extension = None) -> list:
		"""
		List all the files in the given path with the given extension, it gets
		all the files with all the extension if no extension is provided.
		
		:param      path:       The path
		:type       path:       str
		:param      extension:  The extension
		:type       extension:  str
		
		:returns:   List of files
		:rtype:     list
		"""
		try:
			if extension:
				return [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name)) and name.endswith(extension)]
			else:
				return [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
		except FileNotFoundError:
			return f"Error: The directory '{path}' does not exist."
		except PermissionError:
			return f"Error: Permission denied for accessing '{path}'."


	@staticmethod
	def list_all_files_recursive(path: str, extension = None) -> list:
		"""
		List all files in the given dir and in all the subdirs of that directory
		
		:param      path:       The path
		:type       path:       str
		:param      extension:  The extension
		:type       extension:  str
		
		:returns:   The list of files
		:rtype:     list
		"""
		files = FileManager.list_files(path, extension)
		dirs = FileManager.list_dirs(path)
		for d in dirs:
			files += FileManager.list_all_files_recursive(path=os.path.join(path, d), extension=extension)
		return files
		

	@staticmethod
	def dir_exist(f_name: str) -> bool:
		"""
		Checks if a dir exists or not

		:param      f_name:  The file name
		:type       f_name:  str

		:returns:   True if the dir exsits, false otherwise
		:rtype:     bool
		"""
		return os.path.isdir(f_name)


	@staticmethod
	def create_dir(f_name: str, path=''):
		"""
		Creates a dir.
		
		:param      f_name:  The dir name
		:type       f_name:  str
		:param      path:    The path
		:type       path:    str
		"""
		try:
			os.makedirs(path + f_name)
		except FileExistsError:
			pass # There is no problem is the file already exists
		except Exception as e:
			error = f"Error while creating dir '{f_name}': {e}"
			ErrorHandler.log_error(error, e)


	@staticmethod
	def create_dir_hierarchy(data: list, path: str) -> list:
		"""
		Creates a dir hierarchy recursively.. If a data element is a list, then
		that full list of dirs will be created under the previous data element or
		each of the previous data elements in case this was a list. Each of the
		elements in data will be a father of all the next elements of type list in
		data.
		Example [A, B, C]
			A
			∟	B
				∟	C
		Example [[A, B], X, Y, Z]:
			A
			∟	X
				∟	Y
					∟	Z
			B
			∟	X
				∟	Y
					∟	Z
		:param      data:  The the hierarchy list of directory names.
		:type       data:  list
		:param      path:  The path
		:type       path:  str
		
		:returns:   List with the created paths
		:rtype:     list
		"""
		path_list = []
		for i in range(0, len(data), 1):
			if type(data[i]) == list:
				path_l = FileManager.create_dir_hierarchy(data = data[i], path = path)
				for j in path_l:
					FileManager.create_dir_hierarchy(data = data[i + 1:], path = j)
				break
			elif FileManager.dir_exist(path):
				new_path = path + '/' + data[i]
				if(not FileManager.dir_exist(new_path)):
					FileManager.create_dir(f_name = new_path)
					path_list.append(new_path)
		return path_list


	@staticmethod
	def delete_dir(path: str):
		"""
		Deletes a dir and all the content in it

		:param      path:  The path
		:type       path:  str
		"""
		if FileManager.dir_exist(path):
			shutil.rmtree(path)


	@staticmethod
	def get_current_dir() -> str:
		"""
		Gets the current dir.

		:returns:   The current dir.
		:rtype:     str
		"""
		return os.getcwd() + '/'