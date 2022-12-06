import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Mohanlal.xlsx")

print(df.head())

"""
year = df['Year'] < 2000
m_name = df.loc[df['Movie Name']]

print(year)
#print(m_name)
#plt.scatter()
"""
