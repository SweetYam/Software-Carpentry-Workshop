import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


"""Perform regression analysis on mosquito data
    
    1. Takes a dataframe as input that includes columns named 'temperature',
    'rainfall', and 'mosquitos', and
	2. takes figure_filename to save and name data plot.
        
    3. Performs a multiple regression to predict the number of mosquitos.
    4. Creates an observed-predicted plot of the result and saves data plot using specified filename
    5. returns the parameters of the regression.
    
    """
def analyze(data, figure_filename):
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    plt.savefig(figure_filename)
    plt.show()
    return parameters


""" convert fahrenheit to Celsius"""
def fahr_to_celsius(temperature_fahr):
    temperature_celsius = (temperature_fahr - 32) * 5 / 9.0
    return temperature_celsius
	
