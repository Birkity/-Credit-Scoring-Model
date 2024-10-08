from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)

model = load('../notebooks/credit_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])
    
    prediction = model.predict(input_data)[0]  
    
   
    prediction_str = str(prediction)
    
    return jsonify({'prediction': prediction_str})

if __name__ == '__main__':
    app.run(debug=False)
