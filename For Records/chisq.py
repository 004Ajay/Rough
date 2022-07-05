x = [50,60,47,48,70]
exp = 50
y = 0
for i in x:
    y = y+(((i-exp) * (i-exp))/exp)
print("Value: ", y)

#-------------------------------------------------------------------------------------------------------------------#

female = [60, 54, 46, 41]
male = [40, 44, 53, 57]
fem_total = 201
male_total = 194
grand_total = 395
row_total = [100, 98, 99, 98]

fem_mul = (201/395)
male_mul = (194/395)

female_col_mul = []
male_col_mul = []
female_Es = []
male_Es = []

for i in range(len(row_total)):
    fem_row_mul = (row_total[i] * fem_mul)
    male_row_mul = (row_total[i] * male_mul)
    female_col_mul.append(fem_row_mul)
    male_col_mul.append(male_row_mul)
   
print("Female column_mul: ", female_col_mul)
print()
print("Male column_mul: ", male_col_mul)
print()

O = female +  male
E = female_col_mul + male_col_mul

# O : Observed Values, E : Expected Value
print("Concatenated obs: ", O)
print()
print("Concatenated Exps:", E)
print()

res = 0
for i in range(len(O)):
    res = res + (((O[i] - E[i]) * (O[i] - E[i]))/E[i])
print("Chi Sq Value: ", res)

#-------------------------------------------------------------------------------------------------------------------#

#To find probability:

import scipy.stats as stats
res = stats.chisquare(O, E)
lst = list(res)
print(res)
if lst[1] > 0.05:
    print("We accept Null Hypothesis, since", round(lst[1], 5), "is greater than 0.05")