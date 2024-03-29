import os
import sys
from exception import CustomException
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from data_transformation import DataTransformation,DataTransformationConfig
from model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str= os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiat_data_ingestion(self):
        logging.info('entered into the data ingestion component')
        try:
            df = pd.read_csv('notebook\data.csv')
            logging.info('Read the dataset as DataFrame')
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            logging.info('train test split initiated')
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=32)
            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header = True)
            logging.info('Ingestion of the data is completed')

            return (self.data_ingestion_config.train_data_path,
                     self.data_ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)



if __name__=='__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiat_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_file = data_transformation.initiate_data_transformation(train_path=train_data, test_path=test_data)
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
