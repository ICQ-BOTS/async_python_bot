import logging
import sys
from logging.handlers import RotatingFileHandler
import os

log = logging.getLogger(__name__)


class DynamicRotatingFileHandler(RotatingFileHandler):
    def __init__(self, filename, backupCount=1, encoding=None, delay=False):
        dir_name = os.path.dirname(filename)
        file_name = os.path.basename(filename)
        script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        filename = os.path.join(dir_name, script_name + file_name)

        if dir_name:
            try:
                os.makedirs(dir_name)
            except OSError:
                if not os.path.isdir(dir_name):
                    raise

        super(DynamicRotatingFileHandler, self).__init__(
            filename=filename, backupCount=backupCount, encoding=encoding, delay=delay
        )