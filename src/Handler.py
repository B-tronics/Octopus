#######################################################################
#   Class: Handler (Handler.py)
#
#   Author: Supper Balint
#   Date: 2020.10.27
#
#   Handlers send the LogRecord to the required output destination, 
#   like the console or a file. Handler is a base for subclasses like
#   StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. 
#   These subclasses send the logging outputs to corresponding 
#   destinations, like sys.stdout or a disk file.
#######################################################################

class Handler(object):
    def __init__(self):
        raise NotImplementedError