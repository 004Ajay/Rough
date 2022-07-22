# Maths problem calculation

import math
import statistics

x = [10, 12, 15, 30, 25, 27, 32]
y = [70, 2, 80, 100, 11, 16, 7]

n = len(x)
x_mean = statistics.mean(x)
y_mean = statistics.mean(y)
xy_bar = x_mean * y_mean

XiYi = 0
Xi_sq = []
Yi_sq = []

for i in range(len(x)):
    Xi_sq.append(x[i]*x[i])
    Yi_sq.append(y[i]*y[i])
    XiYi += x[i] + y[i]
    
Xi_sq_sum = sum(Xi_sq)
Yi_sq_sum = sum(Yi_sq)

Pxy = ((1/n)*XiYi) - xy_bar
sig_x = math.sqrt(((1/n)*Xi_sq_sum) - x_mean)
sig_y = math.sqrt(((1/n)*Yi_sq_sum) - y_mean)

r = Pxy / (sig_x * sig_y)

print("x\ty\tXiYi\tXi_sq\tYi_sq")
for i in range(len(x)):
    print(f"{x[i]}\t{y[i]}\t{XiYi[i]}\t{Xi_sq[i]}\t{Yi_sq[i]}")
    
print(f"Pxy: {round(Pxy, 4)}\tsigma x: {round(sig_x, 4)}\tsigma_y: {round (sig_y, 4)}")    
