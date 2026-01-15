import sys
import numpy as np
from src.exception import CustomException
from imblearn.over_sampling import SMOTE


class FeatureEngineering:
    def apply_smote(self,x_train,y_train):
        try:
            smote = SMOTE(random_state=42)
            x_train_balanced,y_train_balanced = smote.fit_resample(x_train, y_train)
            
            return x_train_balanced, y_train_balanced

        except Exception as e:
            raise CustomException(e,sys)


