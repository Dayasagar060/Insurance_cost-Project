from flask import Flask, jsonify, request, render_template
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline


app = Flask(__name__)
predictor = PredictPipeline()


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
           
            data = {
                'age': int(request.form['age']),
                'sex': request.form['sex'],
                'bmi': float(request.form['bmi']),
                'children': int(request.form['children']),
                'smoker': request.form['smoker'],
                'region': request.form['region']
            }

           
            input_df = pd.DataFrame([data])

           
            prediction = predictor.predict(input_df)
            prediction = round(float(prediction[0]), 2)

        except Exception as e:
            # Handle any errors gracefully
            return render_template('index.html', prediction=f"Error: {str(e)}")

   
    return render_template('index.html', prediction=prediction)


@app.route('/predict', methods=['POST'])
def predict_api():

    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        prediction = predictor.predict(input_df)
        return jsonify({'prediction': float(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

if __name__ == "__main__":
    app.run(debug=True)