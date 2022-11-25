import pandas as pd
data = pd.read_csv('NB.csv')
wea = data.loc[:, 'Outlook']
temp = data.loc[:, 'Temperature ']
hum = data.loc[:, 'Humidity']
wind = data.loc[:, 'Wind']
play = data.loc[:, 'Play Tennis']

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
wea_enco = le.fit_transform(wea)
temp_enco = le.fit_transform(temp)
hum_enco = le.fit_transform(hum)
wind_enco = le.fit_transform(wind)
label = le.fit_transform(play)
print(f"Weather: {wea_enco}\nTemperature: {temp_enco}\nHumidity: {hum_enco}\nWind: {wind_enco}")

features = list(zip(wea_enco, temp_enco, hum_enco, wind_enco))

from sklearn.naive_bayes import GaussianNB
NB = GaussianNB().fit(features, label)

w = int(input("Weather Label: 0 - Overcast, 1 - Rainy, 2 - Sunny: "))
x = int(input("Temperature Label: 0 - Cool, 1 - Hot, 2 - Mild: "))
y = int(input("Humidity Label: 0 - High, 1 - Normal: "))
z = int(input("Wind Label: 0 - Weak, 1 - Strong: "))

print("Prediction for Play: ", le.inverse_transform(label[NB.predict([[w, x, y, z]])]))