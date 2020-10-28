"""
Class: Logger (Logger.py)

Author: Supper Balint
Date: 2020.10.27

This is the class whose objects will be used in the application 
code directly to call the functions.
"""

import logging


class Logger(object):

    # Number of class instance.
    __instance = None

    # Logger instance.
    __logger = None

    # Logging file name
    __logFileName = None

    # Log level to be set
    __logLevel = None

    # Define class instantiation as Singleton.
    def __new__(cls, val):
        if Logger.__instance is None:
            Logger.__instance = object.__new__(cls)
        Logger.__instance.val = val
        Logger.__logger = logging.getLogger(Logger.__instance.val)
        return Logger.__instance

    def startLogging(self, level):
        """
        Start logging with defined logging level.

        Parameters
        -----------
        level: logging level to be used
                -DEBUG : 10
                -INFO : 20
                -WARNING : 30
                -ERROR : 40
                -CRITICAL : 50
        """
        Logger.__logger.setLevel(level)
        file_handler = logging.FileHandler(f'{Logger.__logFileName}.log')
        formatter = logging.Formatter(
            '%(levelname)s:%(name)s:%(message)s:%(asctime)s')
        file_handler.setFormatter(formatter)
        Logger.__logger.addHandler(file_handler)

        if int(level) == 10:
            Logger.__logger.debug("Logging started!")
        elif int(level) == 20:
            Logger.__logger.info("Logging started!")
        elif int(level) == 30:
            Logger.__logger.warning("Logging started!")
        elif int(level) == 40:
            Logger.__logger.error("Logging started!")
        elif int(level) == 50:
            Logger.__logger.critical("Logging started!")
        else:
            raise ValueError

    @property
    def logFileName(self):
        """Get current output file name."""

        return Logger.__logFileName

    @logFileName.setter
    def logFileNameSetter(self, name):
        """Set output file name."""

        Logger.__logFileName = name
