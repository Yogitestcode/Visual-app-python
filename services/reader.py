import os
import pandas as pd
import chardet

from core.config import Config as cfg
def read_csv() -> list:
    path = os.path.join(cfg.DATA_DIR, "data.csv")

    with open(path, 'rb') as f:
        result = chardet.detect(f.read())
        csv_file = pd.read_csv(path, encoding=result['encoding'])
    return list(csv_file)
