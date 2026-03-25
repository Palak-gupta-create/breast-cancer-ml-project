import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():

    texture = float(request.form["query1"])
    perimeter = float(request.form["query2"])
    smoothness = float(request.form["query3"])
    compactness = float(request.form["query4"])
    symmetry = float(request.form["query5"])

    data = [[texture, perimeter, smoothness, compactness, symmetry]]

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Patient has Breast Cancer"
    else:
        result = "Patient does not have Breast Cancer"

    return render_template("home.html", output=result)

if __name__ == "__main__":
    app.run(debug=True)
