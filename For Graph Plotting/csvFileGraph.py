
"""
----------------------
INCOMPLETE
----------------------
INCOMPLETE
----------------------
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ADL_202_ex.csv') # Opening CSV File 

# Table of Student's information
print("Student's Information\nTotal\tMales\tFemales") # Headings
print("{}\t{}\t{}".format(df['Gender'].count(), 
                          df['Gender'].value_counts().m,
                          df['Gender'].value_counts().f)) #format() used

col1 = df['Mark'] # Gettting & storing MARKS to col1 
col2 = df['Gender'] # Gettting & storing GENDER to col2

# Table of Mean, Max, Min & Class Average
print("\n\nClass Average:", int(col1.mean()),
      "\nMedian:", col1.median(),
      "\nMode:", col1.mode()) # showing mean, median & mode

"""
----------------------
INCOMPLETE
----------------------
INCOMPLETE
----------------------
"""