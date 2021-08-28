from flask import Flask, request, render_template
#from flask_cors import CORS, cross_origin
import util

app = Flask(__name__)
#cors = CORS(app)


@app.route('/')
def index():
    car_models = util.get_car_model_names()
    if car_models[0] != 'Select Car Model':
        car_models.insert(0, 'Select Car Model')
    fuel_types = util.get_car_Fuel()
    if fuel_types[0] != "Select Car's fuel type":
        fuel_types.insert(0, "Select Car's fuel type")
    car_conditions = util.get_car_Condition()
    if car_conditions[0] != "Select Car's condition":
        car_conditions.insert(0, "Select Car's condition")

    return render_template('index.html', car_models=car_models, fuel_types=fuel_types, car_conditions=car_conditions)


@app.route('/predict', methods=['POST'])
#@cross_origin()
def predict():
    car_models = request.form.get('car_models')
    fuel_types = request.form.get('fuel_types')
    car_conditions = request.form.get('car_conditions')
    year = int(request.form.get('year'))
    kilo_driven = int(request.form.get('kilo_driven'))
    # print(car_models,fuel_types,car_conditions,year,kilo_driven)
    prediction = util.get_estimated_price(car_models, fuel_types, car_conditions, year, kilo_driven)

    # print(prediction)

    return str(prediction)


if __name__ == "__main__":
    print('Starting Python Flask Server for Home Price Predictions..')
    util.load_saved_artifacts()
    app.run()
