import pandas as pd
import sys
import pickle
from src.exception import CustomException
from config import model_path

class prediction:
    def __init__(self):
        with open(model_path,"rb") as f:
            self.model = pickle.load(f)

    def predict(self,Data):
        try:
            model = self.model
            Data_df = pd.DataFrame([Data])
            prediction = model.predict(Data_df)
            if prediction==1:
                return 'Rain'
            else:
                return 'No Rain'
            
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    model = prediction()
    data = {"Temperature":24,
    "Humidity":38,
    "Wind_Speed":14,
    "Cloud_Cover":45,
    "Pressure":1002}
    result = model.predict(data)
    print(data)
    print(result)