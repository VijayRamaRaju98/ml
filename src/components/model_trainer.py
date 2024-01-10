import pandas as pd
import numpy as np
from dataclasses import dataclass

from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor,RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from exception import CustomException
from logger import logging
from utils import save_object
from sklearn.linear_model import LinearRegression
import os,sys
from utils import evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path:str = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    
    def initiate_model_trainer(self, train_array, test_array):

        try:
            logging.info('Spliting train and test input data')
            x_train, y_train, x_test, y_test = (train_array[:,:-1], 
                                                train_array[:,-1],
                                                test_array[:,:-1], 
                                                test_array[:,-1])
            

            models = {
                'Random Forest':RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Gradient Boosting':GradientBoostingRegressor(),
                'Linear Regression': LinearRegression(),
                'k neibhour': KNeighborsRegressor(),

            }
        
            model_report:dict = evaluate_model(x_train=x_train, y_train=y_train,
                                                x_test=x_test,y_test=y_test, models = models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException('No best model found')
            
            
            preprocessor_obj = save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)

            predicted = best_model.predict(x_test)

            r2_square = r2_score(y_test,predicted)

            return r2_square

        except Exception as e:
            raise CustomException(e,sys)

