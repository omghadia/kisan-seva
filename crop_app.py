import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

model = joblib.load('/Users/omghadia/Desktop/Crop-Recommendation-system-/Crop recommendation system/crop_app1')

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index2.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    
    # Retrieve other form fields
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Ph = float(request.form['ph'])
    Rainfall = float(request.form['Rainfall'])
    
    if 0 < Ph <= 14 and 0 < Temperature < 100 and 0 < Humidity < 100:
        # Process the form data and make predictions
        values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
        arr = [values]
        prediction = model.predict(arr)
        return render_template('prediction.html', prediction=str(prediction))
    else:
        return "Sorry... Error in entered values in the form. Please check the values and fill them again."

if __name__ == '__main__':
    app.run(debug=True)
