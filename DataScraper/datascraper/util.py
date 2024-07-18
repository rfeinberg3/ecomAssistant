import os
import re
import typing

class ScraperUtil:
    def __init__(self) -> None:
        pass

    def get_filenames(self, directory: str, file_type: str = '.*') -> 'list[str]':
        """ Gets name of each keywords file in keywords directory.
        ### Args:
            directory: The path to the directory you would like the file names of.
            file_type: Returns the names of file only with the given extension. (default = all files)  

        ### Returns:
            List of file names from the directory specified.
        """
        pattern = re.compile(f'{file_type}$')
        return [file for file in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, file)) and pattern.search(file)]
    
    def read_files(self, directory: str, list_of_filenames: 'list[str]') -> 'list[str]':
        """ Reads in the data line by line for each file name given in the given directory path. 
        ### Args
            directory: The path to the directory to read in file data.
            list_of_filenames: The list of files by name you want to read into the return list.
        ### Returns
            data_list: A list of data (as string lines) from each line in each file read in.
        """
        data_list = []
        for file_name in list_of_filenames:
            with open(directory+'/'+file_name, 'r') as file:
                data = file.readlines()
                data_list.extend(data)
        return data_list

