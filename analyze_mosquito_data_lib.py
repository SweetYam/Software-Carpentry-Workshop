import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def analyze(data):
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    plt.show()
    return parameters
	
def fahr_to_celsius(temperature_fahr):
    temperature_celsius = (temperature_fahr - 32) * 5 / 9.0
    return temperature_celsius
	