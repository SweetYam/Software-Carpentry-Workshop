import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

# read the data
data = pd.read_csv(filename)

# convert temperature data in A1_mosquito_data.csv file,
# to fahr using fahr_to_celsius function from mosquito_lib file
data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"])


print data.head()

parameters = mosquito_lib.analyze(data, "plot.jpg")

#instead of printing parameters via "print parameters", instead we save in a new file
#Save parameters to file
parameters.to_csv("parameters.csv")


