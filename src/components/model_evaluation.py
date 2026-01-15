import sys
from src.exception import CustomException
from sklearn.metrics import accuracy_score, classification_report

class EvaluateModel:
    def evaluate(self,x_test,y_test,model):
        try:
            y_pred = model.predict(x_test)
            return {accuracy_score(y_test,y_pred), classification_report(y_test,y_pred)}

        except Exception as e:
            raise CustomException(e,sys)