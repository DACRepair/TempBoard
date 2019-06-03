import os
from configparser import ConfigParser as _CP


class ConfigParser(_CP):
    def __init__(self):
        self.conf_file = None
        super().__init__()

    def read(self, filenames, encoding=None):
        super().read(filenames, encoding)
        self.conf_file = filenames

    def _write_file(self):
        with open(self.conf_file, 'w') as file:
            self.write(file)
            file.close()
        self.read(self.conf_file)

    def add_section(self, section):
        super().add_section(section)
        self._write_file()

    def set(self, section, option, value=None):
        super().set(section, option, value)
        self._write_file()


Config = ConfigParser()
Config.read(os.path.normpath(os.getcwd() + "/config.ini"))
