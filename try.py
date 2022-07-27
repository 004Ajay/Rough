# Question: Calculation pearson r value for the given x & y values

import math, statistics

y = []

y_real = [370, 340, 375, 310, 350, 200, 400, 375, 285, 225, 345, 285]

for i in y_real:
    y.append(round((i/60), 4))

x = [4200, 3600,  3750, 3675, 4050, 2770, 4870, 4500, 3450, 2700, 3750, 3300]

n_div = 1/len(x)
x_mean = round(statistics.mean(x), 4) # calculating mean (x)
y_mean = round(statistics.mean(y), 4) # calculating mean (y)
x_mean_sq = round(x_mean * x_mean, 4) # calculating sq of mean (x)
y_mean_sq = round(y_mean * y_mean, 4) # calculating sq of mean (y)
xy_bar = round(x_mean * y_mean, 4) # finding x̄ȳ

XiYi, Xi_sq, Yi_sq = [], [], [] # declaring multiple lists
Xi_sq_sum, Yi_sq_sum, XiYi_sum = 0, 0, 0 # initializing multiple variables to 0

for i in range(len(x)): # calculating square of each observation in x & y
    Xi_sq.append(round(x[i]*x[i], 4)) # calculating square of Xi
    Yi_sq.append(round(y[i]*y[i], 4)) # calculating square of Yi
    XiYi.append(round(x[i]*y[i], 4)) # calculating square of Xi*Yi
    
Xi_sq_sum = sum(Xi_sq) # calculating sum of Xi^2 values
Yi_sq_sum = sum(Yi_sq) # calculating sum of Yi^2 values
XiYi_sum = sum(XiYi) # calculating sum of XiYi values

Pxy = ((n_div) * XiYi_sum) - xy_bar # calculating Pxy
sig_x = math.sqrt(((n_div) * Xi_sq_sum) - x_mean_sq) # calculating σx
sig_y = math.sqrt(((n_div) * Yi_sq_sum) - y_mean_sq) # calculating σy
r = Pxy / (sig_x * sig_y) # calculating pearson r

print(f"\n{'-'*73}\n| x\t|\ty\t|\tXiYi\t|\tXi_sq\t|\tYi_sq\t|\n{'-'*73}") # Table 'headings' with line separation
for i in range(len(x)):
    print(f"| {x[i]}\t|\t{y[i]}\t|\t{XiYi[i]}\t|\t{Xi_sq[i]}\t|\t{Yi_sq[i]}\t|\n{'-'*73}") # Table 'values' with line separation
print(f"\nx̄: {x_mean}\t|\tȳ: {y_mean}\t|\tx̄ȳ: {xy_bar}\t|\tΣXiYi: {XiYi_sum}\t|\n") # Printing calculated values
print(f"\nx̄^2: {x_mean_sq}\t|\tȳ^2: {y_mean_sq}\t|\tΣXi^2: {Xi_sq_sum}\t|\tΣYi^2: {Yi_sq_sum}\t|\n\n{'-'*90}")     
print(f"\nPxy: {round(Pxy, 4)}\t|\tσx: {round(sig_x, 4)}\t|\tσy: {round (sig_y, 4)}\t|\tr: {round(r, 4)}\n\n{'-'*90}")