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
import logging

# instantiate logger
log = logging.getLogger(__name__)

def main():

	log.info("This is a log message")

if __name__ == '__main__':
    main()
