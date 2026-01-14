import sys
from src.components.data_ingestion import data_ingestion
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class validationconfig:
    required_cols = ['Temperature','Humidity','Wind_Speed','Cloud_Cover','Pressure','Rain']

class validation:
    def __init__(self):
        self.req_cols = validationconfig()

    def validate(self,data_df):
        data_cols = data_df.columns
        req_cols = self.req_cols.required_cols

        try:
            if req_cols != list(data_cols):
                missing_cols = set(req_cols) - set(data_cols)
                raise ValueError(f"Required columns are missing - {missing_cols}")
            
            if data_df.empty:
                raise ValueError("Dataset is empty")
            
            duplicates = data_df.duplicated().sum()

            return{
                'status': 'success',
                'duplicates' : int(duplicates)
            }

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    data = data_ingestion().Ing_data()
    validation= validation().validate(data)
    print(validation)
        