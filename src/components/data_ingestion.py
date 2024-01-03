import sys
import pandas as pd
from dataclasses import dataclass
import os



@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    data_path:str = os.path.join('artifacts', 'data.csv')


class Initiate_Data_ingestion():
    def __init__(self):
        self.data_ingestion_config =DataIngestionConfig()

    def initiate_data_ingetion(self):
        data = pd.read_csv()