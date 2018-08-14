import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IO_PATH = '%s/io/user' % BASE_DIR

LOG_FORMAT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"

GOODS = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
