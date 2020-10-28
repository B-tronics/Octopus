#######################################################################
#   File: main.py
#
#   Author: Supper Balint
#   Date: 2020.10.26
#
#   Main file which controls all the objects instanciated.
#   Entry point is defined in this file.
#######################################################################


from src import Logger as log


def main():
    logger = log.Logger(__name__)
    logger.logFileNameSetter = 'output'

    try:
        logger.startLogging(log.logging.DEBUG)
    except ValueError:
        print(ValueError)
    return 0


if __name__ == '__main__':
    main()
