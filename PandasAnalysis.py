# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series(['Coast Redwood', 'Yellow Meranti', 'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'])
series.index=(['a', 'b', 'c', 'd', 'e'])

print(series)

series = pd.Series({'a':'Coast Redwood', 'b':'Yellow Meranti', 'c':'Mountain Ash', 'd':'Coast Douglas Fir', 'e':'Sitka Spruce'})
series2 = pd.Series({'a': 380.3, 'b': 331, 'c': 329.7, 'd': 327, 'e': 317})

df = pd.DataFrame(index=['a', 'b', 'c', 'd', 'e'], 
data={'name': ['Coast Redwood', 'Yellow Meranti', 'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'], 'height': [380.3, 331, 329.7, 327, 317]})
df = pd.DataFrame({'name': series, 'height': series2})

print(df)

# Titanic
df = pd.read_csv('./titanic.csv')
pd.set_option('display.max_rows', None)
print(df.isnull().sum())

df.dropna(inplace=True)
df.drop(['Embarked'], inplace=True, axis='columns')

df[df['Sex'] == 'male']
first = df[df['Pclass'] == 1].reset_index()
print(df.nlargest(100, 'Fare'))
print(df.groupby(['Pclass']).count())
print(df.groupby(['Pclass'])['PassengerId'].count())
print(df.groupby(['Pclass']).mean())
print(df.groupby(['Pclass', 'Sex'])['Survived'].mean())
# Other important methods are .describe and .corr

df.hist(column='Age', by='Pclass')
df.plot.scatter(x='Age', y='Fare')

weather = pd.read_csv('./weather.csv')
weather.dropna(inplace=True)
weather.reset_index(inplace=True)
weather.drop(['index'], inplace=True, axis='columns')

weather.plot.line(x='datetime', y='station_london')

print(weather.iloc[0:50])

weather.iloc[0:50].plot.line(x='datetime', y='station_london')

plt.show()
