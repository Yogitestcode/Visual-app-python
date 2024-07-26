import os

from pathlib import Path


class Config(object):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = os.path.join(BASE_DIR, "data")
    TEMPLATE_DIR = os.path.join(os.path.join(BASE_DIR, 'src'),'templates')

                                             