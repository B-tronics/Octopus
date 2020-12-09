#######################################################################
#   File: main.py
#
#   Author: Supper Balint
#   Date: 2020.10.26
#
#   Main file which controls all the objects instanciated.
#   Entry point is defined in this file.
#######################################################################
from helpers import logger
from helpers import detector
import logging

# instantiate logger
log = logging.getLogger(__name__)


from src import Logger as log


def main():
<<<<<<< HEAD
    logger = log.Logger(__name__)
    logger.logFileNameSetter = 'output'

    try:
        logger.startLogging(log.logging.DEBUG)
    except ValueError:
        print(ValueError)
    return 0


=======

>>>>>>> logging
if __name__ == '__main__':
    main()
