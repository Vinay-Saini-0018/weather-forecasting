import sys
import numpy as np
from sklearn.model_selection import train_test_split
from src.components.data_ingestion import data_ingestion
from src.exception import CustomException

class transform:

    def transformation(self,data):
        try:
            rounded_df = np.round(data,decimals=2)

            rounded_df['Rain'] = rounded_df['Rain'].replace({
                "rain": 1,
                "no rain": 0
            })

            x = rounded_df.drop(columns=["Rain"])
            y = rounded_df["Rain"]
            x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

            return x_train,x_test,y_train,y_test

        except Exception as e:
            raise CustomException(e,sys)
        
'''if __name__ == "__main__":
    data = data_ingestion().Ing_data()
    _,_,y_train,y_test= transform().transformation(data)
    print(y_train)'''