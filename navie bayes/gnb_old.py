import pandas as pd
data = pd.read_csv('NB.csv')
wea = data.loc[:, 'Outlook']
temp = data.loc[:, 'Temperature ']
hum = data.loc[:, 'Humidity']
wind = data.loc[:, 'Wind']
play = data.loc[:, 'Play Tennis']

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

wea_encoded=le.fit_transform(wea)
print("Weather:", wea_encoded)

temp_encoded=le.fit_transform(temp)
print("Temperature:", temp_encoded)

hum_encoded=le.fit_transform(hum)
print("Humidity:", hum_encoded)

wind_encoded=le.fit_transform(wind)
print("Wind:", wind_encoded)

label=le.fit_transform(play)
print("Play:", label)


features = zip(wea_encoded, temp_encoded, hum_encoded, wind_encoded)
lis = list(features)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB().fit(lis,label)

w = int(input("Weather Label: 0 - Overcast, 1 - Rainy, 2 - Sunny: "))
x = int(input("Temperature Label: 0 - Cool, 1 - Hot, 2 - Mild: "))
y = int(input("Humidity Label: 0 - High, 1 - Normal: "))
z = int(input("Wind Label: 0 - Weak, 1 - Strong: "))

predicted= model.predict([[w, x, y, z]])
print("Prediction for Play: ", le.inverse_transform(label[predicted]))