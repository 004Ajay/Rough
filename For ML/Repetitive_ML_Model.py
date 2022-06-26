import tensorflow as tf
import numpy as np
from tensorflow import keras

while True:
   model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
   model.compile(optimizer='sgd', loss='mean_squared_error')

   xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
   ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
   # y = 2x-1

   model.fit(xs, ys, epochs=500)
   
   num = int(input("Enter num to predict: "))
   print(model.predict([num]))

   if input("Trying again? y/n : ") != 'y':
    break