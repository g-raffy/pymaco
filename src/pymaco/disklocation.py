from pathlib import Path

class IDiskLocation(object):

    pass

class IsoDiskLocation(IDiskLocation):

    def __init__(self, iso_file_path):
        """:param Path iso_file_path: location of the iso file
        """
        self.iso_file_path = iso_file_path


