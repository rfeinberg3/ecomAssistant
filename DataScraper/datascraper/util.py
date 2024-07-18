import os
import re
import typing

class ScraperUtil:
    def __init__(self) -> None:
        pass

    def get_filenames(self, directory: str, file_type: str = '.*') -> list[str]:
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
    
