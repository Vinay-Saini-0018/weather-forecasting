import pandas as pd
import sys
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class Ingestionconfig:
    data_location: str = "data/raw/Weather forecast data.csv"

class data_ingestion:
    def __init__(self):
        self.dataconfig = Ingestionconfig()

    def Ing_data(self):
        try:
            data_path = self.dataconfig.data_location
            data = pd.read_csv(data_path)
            return data
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    data_ingestion = data_ingestion()
    print(data_ingestion.Ing_data())