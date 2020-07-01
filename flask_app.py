# Dependent libraries
# For API
from flask import Flask, request, jsonify
# For model
import pickle
# For traceback error
import traceback
# For Manipulating the data
import pandas as pd
# For Mathametical calculations
import numpy as np

# API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])

# Function to predict the survival
def predict():
    if model:
        try:
            # json post to API
            input_json = request.json
            print(input_json)
            # Dummy variables for the input features
            query = pd.get_dummies(pd.DataFrame(input_json))
            query = query.reindex(columns=model_columns, fill_value=0)
            # Predict the outcome
            predicted = list(model.predict(query))
            prediction= [ "Survived" if x==1 else "Not Survived" for x in predicted ]
            return jsonify({'prediction': prediction})
        # exception with traceback
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        return ('No model found')

if __name__ == '__main__':
    try:
        # command-line input
        port = int(sys.argv[1]) 
    except:
        # default port if port is not specified
        port = 12345 
    # Load "model.pkl"
    model = pickle.load( open( "model.pkl", "rb" ) ) 
    print ('Model loaded')
    # Load "model_columns.pkl"
    model_columns = pickle.load( open( "model_columns.pkl", "rb" ) ) 
    print ('Model columns loaded')
    # Run the API app
    app.run(port=port, debug=True)