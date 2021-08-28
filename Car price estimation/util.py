import json
import pickle
import numpy as np

__car_model = None
__Fuel = None
__Condition = None
__data_columns: None = None
__load_model = None


def get_estimated_price(car_model, fuel, condition, year, km_driven):
    try:
        car_model_index = __data_columns.index(car_model)
        index_fuel = __data_columns.index(fuel)
        index_condition = __data_columns.index(condition)
    except:
        car_model_index = -1
        index_fuel = -1
        index_condition = -1
    x = np.zeros(len(__data_columns))
    x[0] = km_driven
    x[1] = year
    if car_model_index >= 0:
        x[car_model_index] = 1
    if index_fuel >= 0:
        x[index_fuel] = 1
    if index_condition >= 0:
        x[index_condition] = 1
    return round(__load_model.predict([x])[0])


def get_car_model_names():
    return __car_model


def get_car_Fuel():
    return __Fuel


def get_car_Condition():
    return __Condition


def load_saved_artifacts():
    print('loading saved artifacts .... start')
    global __data_columns
    global __car_model
    global __Fuel
    global __Condition

    with open("columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __Fuel = __data_columns[4:9]
        __Condition = __data_columns[2:4]
        __car_model = __data_columns[9:]

    global __load_model
    with open("car_price_estimation.sav", 'rb') as f:
        __load_model = pickle.load(f)
    print('loading saved artifacts...done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_car_model_names())
    print(get_car_Condition())
    print(get_car_Fuel())
    print( get_estimated_price('alto lapin', 'petrol', 'used', 2010, 10000))

