import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('csvFile.csv') # Opening CSV File

OverallMean = df['Mark'].mean() # Mean of whole Dataset
print("Overall Mean mark: ", round(OverallMean, 4), "\n")

# Mean Line Plotting
X_Axis = df['Sl No']
Y_Axis = [OverallMean] * len(X_Axis)
plt.plot(X_Axis, Y_Axis, color='green', linestyle='dotted', label='Mean Line')

# ------------------------------------------------------------------------------------------------------------------------- #

# MALE DATA MANIPULATION
maleData = df.loc[df['Gender'] == 'm'] # Separating Male's Data
print(maleData)