import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-np.pi,np.pi,100)

p = np.sin(x) # y = sin(x)
q = np.sin(-x) # y = sin(2x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,p, 'b-', label='y=sin(x)')
plt.plot(x,q, 'c-', label='y=sin(2x)')
plt.show()

#---------------------
#incomplete
#---------------------