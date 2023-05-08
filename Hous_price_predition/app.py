# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Avg_Area_Income = float(request.form['Avg_Area_Income'])
        Avg_Area_House_Age = float(request.form['Avg_Area_House_Age'])
        Avg_Area_Number_of_Rooms = float(request.form['Avg_Area_Number_of_Rooms'])
        Avg_Area_Number_of_Bedrooms = float(request.form['Avg_Area_Number_of_Bedrooms'])
        Area_Population = float(request.form['Area_Population'])


        Avg_Area_Income = np.log(Avg_Area_Income)
        Avg_Area_House_Age = np.log(Avg_Area_House_Age)
        Avg_Area_Number_of_Rooms = np.log(Avg_Area_Number_of_Rooms)
        Avg_Area_Number_of_Bedrooms = np.log(Avg_Area_Number_of_Bedrooms)
        Area_Population = np.log(Area_Population)

        prediction = model.predict([[Avg_Area_Income, Avg_Area_House_Age, Avg_Area_Number_of_Rooms,
       Avg_Area_Number_of_Bedrooms, Area_Population]])



        return render_template("prediction.html", prediction_text="loan status is {}".format(prediction))




    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)