import statistics as st

X = [42, 34, 25, 35, 37, 38, 31, 33, 19, 29, 38, 28, 29, 36, 18]
Y = [18, 6, 0, -1, 13, 14, 7, 7, -9, 8, 8, 5, 3, 14, -7]

Y_mean = round(st.mean(Y), 4)

# For Y_cap, here 'y_cap' is calculated using => -24.704 + (0.9674*x[i])
Y_cap = []
for i in X:
    each_y_cap = -24.704 + (0.9674 * i)
    Y_cap.append(round(each_y_cap, 4))
    
# For (Y - Y_cap)^2
Y_sq = []
for i in range(len(Y)):
    val = (Y[i] - Y_cap[i]) ** 2 # Squaring
    Y_sq.append(round(val, 4))
    
# For (Y - Y_mean)^2
Y_mean_sq = []
for i in range(len(Y)):
    m_val = (Y[i] - Y_mean) ** 2
    Y_mean_sq.append(round(m_val, 4))
    
Y_sq_sum = round(sum(Y_sq), 4) # SSE
Y_mean_sq_sum = round(sum(Y_mean_sq), 4) # SSR
SST = Y_sq_sum + Y_mean_sq_sum
R_sq = 1-(Y_sq_sum/SST)

from tabulate import tabulate

table = [['col 1', 'col 2', 'col 3', 'col 4', 'col 5', 'col 6', 'col 7', 'col 8', 'col 9', 'col 10', 'col 11', 'col 12', 'col 13', 'col 14', 'col 15'], Y_cap, Y_sq, Y_mean_sq]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))