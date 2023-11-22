import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model from the pickle file
with open('Classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form.to_dict()
        features = [int(data['credit_score']), float(data['geography']), float(data['gender']),
                    int(data['age']), int(data['tenure']), float(data['balance']),
                    int(data['num_of_products']), int(data['has_cr_card']),
                    int(data['is_active_member']), float(data['estimated_salary']),
                    int(data['satisfaction_score']), float(data['card_type']),
                    int(data['point_earned'])]

        # Make a prediction 
        prediction = classifier.predict([features])

        return render_template('index.html', result=f'Churn Prediction: {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
