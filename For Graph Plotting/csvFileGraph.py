import matplotlib.pyplot as plt
import pandas as pd

csvFile = pd.read_csv('ADL_202_ex.csv')

col1 = csvFile['Mark'].tolist()
col2 = csvFile['Gender'].tolist()

plt.grid()
plt.title("Students Mark Graph")
plt.scatter(col1, col2)
plt.xlabel('Mark')
plt.ylabel('Gender')
plt.show()
