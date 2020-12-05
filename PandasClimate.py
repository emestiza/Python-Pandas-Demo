# https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Import the csv data:
df = pd.read_csv('GlobalTemperatures.csv')

# Print out data
print(df[['dt', 'LandAverageTemperature', 'LandAverageTemperatureUncertainty']])
# print(data[0:2])

plt.rcParams["figure.figsize"] = [10, 5]
df.plot.line(x = 'dt', y = 'LandAverageTemperature')
df.plot.scatter(x = 'dt', y = 'LandAverageTemperature')

