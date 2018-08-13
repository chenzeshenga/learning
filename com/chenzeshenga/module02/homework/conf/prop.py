import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IO_PATH = '%s/io/user' % BASE_DIR

LOG_FORMAT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
