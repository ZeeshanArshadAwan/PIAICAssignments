# -*- coding: utf-8 -*-
"""MNIST-Fashion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aTJP-oAhjrEomQnIcTb0JJCy8i6Cig6G

Import MNIST-Fashion Dataset 
Name Muhammad Tanveer Sultan PIAIC Roll No 49902
"""

from tensorflow.keras.datasets import fashion_mnist

#spliting traing and testing images data
(train_images,train_labels) , (test_images, test_lables) = fashion_mnist.load_data()

#cheching length of training and testing data
print(len(train_images))
print(len(train_labels))

print(len(test_images))
print(len(test_lables))

#checking the shpes of our data
print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_lables.shape)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

import matplotlib.pyplot as plt
print("class name" , class_names[train_labels[15]])
plt.imshow(train_images[15] , cmap=plt.cm.binary)
plt.show()

#checking unique labels
import numpy as np
print(np.unique(train_labels))
print(np.unique(test_lables))

"""**Preparing the Data for Traing **"""

print(train_images.shape)
train_images=train_images.reshape((60000, 28*28))
print(train_images.shape)
train_images=train_images.astype("float32")/255
print(train_images.shape)

test_images=test_images.reshape((10000, 28*28))
test_images=test_images.astype("float32")/255

"""**Preparing Lables**"""

train_labels[2]

#One Hot Encode
from tensorflow.keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_lables = to_categorical(test_lables)

"""** Creating the Model Netwrok Architecture **"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Flatten , Dropout
from tensorflow.keras.activations import relu ,softmax
from tensorflow.keras.optimizers import RMSprop 
from tensorflow.keras.losses import categorical_crossentropy

network = Sequential()
network.add(Dense(512 , activation=relu , input_shape=(28*28,)))
network.add(Dropout(0.2))
network.add(Dense(10 , activation=softmax))

network.summary()

#compile the Model
network.compile(optimizer='rmsprop' , loss='categorical_crossentropy' , metrics=['acc'])

#Train model
train_images.shape

history=network.fit(train_images, train_labels, epochs=5, batch_size=128)

print(history.history.keys())

#  "Accuracy"
plt.plot(history.history['acc'])
plt.plot(history.history['loss'])
plt.title('model accuracy and loss')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train acc','trian loss'], loc='upper left')
plt.show()

#Evaluate Model
test_loss, test_acc = network.evaluate(test_images , test_lables)



print("losss" , test_loss)

print("model acc" , test_acc)

