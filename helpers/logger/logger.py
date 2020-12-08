""" Logger module configuration"""

import logging.config

logging.config.fileConfig(fname='helpers/logger/config.conf', disable_existing_loggers=False)