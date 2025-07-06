from flask import Flask, request, jsonify
import pickle
import numpy as np

#Loading the model
try:
    with open('./Real_estate_catboost_model.pkl', 'rb') as pkl_file: 
        model = pickle.load(pkl_file)
except Exception as e:
       print(f"Error loading model: {e}")
#Loading the preprocessing pipeline       
try:
    with open('./Real_estate_price_pipeline.pkl', 'rb') as pkl_file: 
        pipeline = pickle.load(pkl_file)
except Exception as e:
    print(f"Error loading model: {e}")

#Initialising the Flask application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    #Features from the request
    features = np.array(request.json)
    #Error if no features are passed
    if features is None:
        return jsonify({'error': 'No features provided'}), 400
    # Reshape to match the model input shape
    features = np.array(features).reshape(1, -1)
    #Processing the features using the pipeline
    processed_features = pipeline.transform(features) 
    #Predicting
    prediction = model.predict(processed_features)
    #Return the prediction
    return  jsonify({'prediction': prediction[0]})

#Running the app
if __name__ == '__main__':
    app.run('localhost', 5000)