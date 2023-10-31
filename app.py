import pickle
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Load the pickled model
with open("rf_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define a route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Define a route to handle predictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user input from the HTML form
        features = [float(request.form[field]) for field in ["credit_score", "geography", "gender", "age", "tenure", "balance", "num_of_products", "has_cr_card", "is_active_member", "estimated_salary"]]

        # Make a prediction using the loaded model
        prediction = model.predict([features])[0]

        # Determine the churn label
        churn_label = "Churn" if prediction == 1 else "Not Churn"

        # Render the result page with the prediction
        return render_template("result.html", prediction=churn_label)

    except Exception as e:
        # Handle exceptions, such as invalid input
        error_message = f"An error occurred: {str(e)}"
        return render_template("result.html", prediction=error_message)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
