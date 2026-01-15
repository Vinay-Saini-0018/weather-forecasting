from flask import Flask,render_template,request,jsonify
from src.pipeline.prediction_pipeline import prediction

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def forecast():
    data = None
    if request.method == 'POST':
        temperature = request.form.get('temperature')
        humidity = request.form.get('humidity')
        wind_speed = request.form.get('wind_speed')
        cloud_cover = request.form.get('cloud_cover')
        pressure = request.form.get('pressure')

        data = {"Temperature":temperature,
                "Humidity":humidity,
                "Wind_Speed":wind_speed,
                "Cloud_Cover":cloud_cover,
                "Pressure":pressure}
        
        model = prediction()
        result = model.predict(data)
        return render_template("index.html", result=result)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)