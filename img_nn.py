"""
image classifying neural network in python
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# load the data
data = keras.datasets.fashion_mnist

# split the data into training and testing sets
(train_images, train_labels), (test_images, test_labels) = data.load_data()

# define the class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# normalize the data
train_images = train_images/255.0
test_images = test_images/255.0

# create the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

# compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# train the model
model.fit(train_images, train_labels, epochs=10)

# test the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Tested Acc:", test_acc)

# make predictions
prediction = model.predict(test_images)

# print the predictions
for i in range(10):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction: " + class_names[np.argmax(prediction[i])])
    plt.show()