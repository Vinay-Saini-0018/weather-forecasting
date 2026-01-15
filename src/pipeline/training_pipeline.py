import os
import pickle
from src.components.data_ingestion import data_ingestion
from src.components.data_validation import validation
from src.components.data_transformation import transform
from src.components.feature_engineering import FeatureEngineering
from src.components.model_trainer import TrainModel
from src.components.model_evaluation import EvaluateModel
from config import model_path


# 1. Ingecting data
data = data_ingestion().Ing_data()

# 2. Validate data
validater = validation()
val = validater.validate(data)

# 3. transformation
x_train,x_test,y_train,y_test = transform().transformation(data)

# 4. feature engineering
x_train_balanced , y_train_balanced = FeatureEngineering().apply_smote(x_train,y_train)

# 5. train model
model = TrainModel().train_model(x_train_balanced,y_train_balanced)

# 6. saving model
os.makedirs('artifacts',exist_ok=True)
with open(model_path,"wb") as f:
    pickle.dump(model,f)

# evaliation matrix
evaluate = EvaluateModel()
accuracy,classification_report = evaluate.evaluate(x_test,y_test,model)
print(f"accuracy score: {accuracy}")
print(f"classification report: \n {classification_report}")


print('pipeline completed')


