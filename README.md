# 🌦️ Weather Forecasting System

A machine learning-based weather forecasting system that predicts whether it will rain or not. This intelligent system analyzes real weather data including temperature, humidity, wind speed, cloud cover, and air pressure to make accurate rain predictions.

## 🌟 Live Demo

Not live

## 📖 About The Project

Weather prediction is crucial for planning daily activities, agriculture, aviation, and many other sectors. This project uses machine learning algorithms to predict rain probability based on multiple weather parameters. Simply input the current weather conditions, and the system will tell you whether it's likely to rain or not!

### How It Works

The system uses **Machine Learning Classification Models** trained on historical weather data. By analyzing patterns in temperature, humidity, wind speed, cloud cover, and atmospheric pressure, the model can accurately predict the likelihood of rainfall.

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Flask** - Web framework for the application
- **Scikit-learn** - Machine learning library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib/Seaborn** - Data visualization
- **Jupyter Notebook** - Model development and analysis
- **HTML/CSS** - Frontend interface


## 🚀 Getting Started

Follow these simple steps to run the project on your local machine:

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/Vinay-Saini-0018/weather-forecasting.git
   cd weather-forecasting
```

2. **Install required packages**
```bash
   pip install -r requirements.txt
```

3. **Run the application**
```bash
   python app.py
```

4. **Open in browser**
```
   Navigate to http://127.0.0.1:5000/ in your web browser
```

## 💡 How to Use

1. **Launch the Application**: Open the web app in your browser
2. **Enter Weather Data**: Fill in the form with current weather conditions
   - Temperature (in °C or °F)
   - Humidity (in %)
   - Wind Speed (in km/h)
   - Cloud Cover (in %)
   - Air Pressure (in hPa)
3. **Get Prediction**: Click "Predict" button
4. **View Result**: See if it will rain or not, along with confidence level


## 🧠 Model Development Process

### Step-by-Step Process:

1. **Data Collection**:
   - Gathered historical weather data with rain labels
   - Data includes temperature, humidity, wind speed, cloud cover, and pressure
   - Dataset contains thousands of weather observations

2. **Exploratory Data Analysis (EDA)**:
   - Analyzed weather patterns and correlations
   - Visualized relationships between different weather parameters
   - Identified key features that influence rainfall

3. **Data Preprocessing**:
   - Cleaned data and handled missing values
   - Normalized numerical features for better model performance
   - Encoded categorical variables if any
   - Split data into training and testing sets

4. **Model Training**:
   - Trained multiple classification models (Logistic Regression, Random Forest, Decision Tree, etc.)
   - Compared model performances
   - Selected the best performing model
   - Fine-tuned hyperparameters for optimal results

5. **Model Evaluation**:
   - Evaluated model using accuracy, precision, recall, and F1-score
   - Created confusion matrix to understand predictions
   - Validated model on test data

6. **Model Deployment**:
   - Saved the trained model using Pickle
   - Created Flask web application
   - Integrated model for real-time predictions

## 🎯 Model Performance

- **Algorithm**: Classification Model (Random Forest/Logistic Regression/Decision Tree)
- **Accuracy**: High accuracy on test data
- **Key Metrics**: Precision, Recall, F1-Score
- **Training Data**: Historical weather data with rain labels
- **Prediction Speed**: Real-time (< 1 second)

## 📈 Features & Improvements

### Current Features:
- ✅ Rain prediction based on 5+ weather parameters
- ✅ Web interface for easy access
- ✅ Real-time predictions
- ✅ Model saved for quick deployment


## 👨‍💻 Author

**Vinay Saini**

- GitHub: [@Vinay-Saini-0018](https://github.com/Vinay-Saini-0018)
