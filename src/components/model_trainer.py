import os 
import sys
from src.exception import CustomException
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

class TrainModel:
    def train_model(self,x_train_balanced,y_train_balanced):
        try:
            params = {
                'n_estimators':[100,120,130,150]
            }

            rfc = RandomForestClassifier()

            grid = GridSearchCV(rfc,param_grid=params)
            grid.fit(x_train_balanced,y_train_balanced)

            print(f"best param: {grid.best_params_}")
            print(f"best model: {grid.best_estimator_}")

            model = grid.best_estimator_
            return model
        
        except Exception as e:
            raise CustomException(e,sys)
