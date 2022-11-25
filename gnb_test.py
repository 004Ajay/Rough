import pandas as pd
data = pd.read_csv('NB.csv')
wea = data.loc[:, 'Outlook']
temp = data.loc[:, 'Temperature ']
hum = data.loc[:, 'Humidity']
wind = data.loc[:, 'Wind']
play = data.loc[:, 'Play Tennis']

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
ls = [wea, temp, hum, wind, play]
wea_en, temp_en, hum_en, wind_en, lb = map(le.fit_transform, ls)
print(f"Weather: {wea_en}\nTemperature: {temp_en}\nHumidity: {hum_en}\nWind: {wind_en}")

features = list(zip(wea_en, temp_en, hum_en, wind_en))

from sklearn.naive_bayes import GaussianNB
NB = GaussianNB().fit(features, lb)

w = int(input("Weather Label: 0 - Overcast, 1 - Rainy, 2 - Sunny: "))
x = int(input("Temperature Label: 0 - Cool, 1 - Hot, 2 - Mild: "))
y = int(input("Humidity Label: 0 - High, 1 - Normal: "))
z = int(input("Wind Label: 0 - Weak, 1 - Strong: "))

print("Prediction for Play: ", le.inverse_transform(lb[NB.predict([[w, x, y, z]])]))