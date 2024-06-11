import sys
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from datetime import datetime
import keras
from sklearn.metrics import roc_curve
from sklearn.metrics import auc


# the phi and psi functions used for the likelihood ratio estimation
def phi(z):
    return -np.square(z)

def psi(z):
    return -np.log(z)

# custom loss function for the neural network from the likelihood ratio estimation
class CustomBinaryCrossentropy(tf.keras.losses.Loss):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.epsilon = tf.keras.backend.epsilon()

    def call(self, y_true, y_pred):
        y_true = tf.cast(y_true, dtype=y_pred.dtype)
        
        psi_signal = -y_true*tf.math.log(y_pred + self.epsilon)
        phi_background = -1*(1-y_true)*tf.math.log(1-y_pred + self.epsilon)

        loss_signal = tf.reduce_sum(psi_signal)
        loss_background = tf.reduce_sum(phi_background)

        # Normalize by the number of samples per category
        loss_signal /= ( tf.reduce_sum(y_true) + self.epsilon )
        loss_background /= (tf.reduce_sum((1 - y_true)) + self.epsilon)

        # Combine the signal and background losses
        total_loss = loss_signal + loss_background
         
        # Combine the signal and background losses
        total_loss = loss_signal + loss_background

        return total_loss

# defining the neural network 
def NeuralNetwork(num_features, nodes, eta, lamda, train, train_label, loss_function):

    # Input variables:
    # num_elements = number of features in the dataset
    # nodes = number of nodes in the hidden layer
    # eta = learning rate
    # lamda = regularization parameter
    # train = training data
    # train_label = training labels
    # loss_function = loss function used
    
    # normalize the data and apply it to the layers
    layer_norm = tf.keras.layers.Normalization()
    layer_norm.adapt(train)
    model = tf.keras.Sequential([layer_norm])

    # add input layer with the number of features
    model.add(layers.Dense(nodes, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(lamda), input_dim=num_features))

    # add two hidden layers
    model.add(layers.Dense(nodes, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(lamda)))
    model.add(layers.Dense(nodes, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(lamda)))
    # add output layer
    model.add(layers.Dense(1, activation='sigmoid'))

    # compile the model with the chosen loss function
    if loss_function == 'binary_crossentropy':
        model.compile(optimizer= tf.keras.optimizers.SGD(
            learning_rate=eta) , loss= 'binary_crossentropy', metrics=['AUC', 'accuracy'])
    elif loss_function == 'custum_binary_crossentropy':
        custom_loss = CustomBinaryCrossentropy()
        model.compile(optimizer= tf.keras.optimizers.SGD(
            learning_rate=eta) , loss=custom_loss, metrics=['AUC', 'accuracy'])

    return model

# User input parameters
grid = str(sys.argv[1])
model = str(sys.argv[2])
Epochs = int(sys.argv[3])
nodes = int(sys.argv[4])
eta = float(sys.argv[5])
lamda = float(sys.argv[6])

# load time
now = datetime.now()
timestamp = now.strftime("%m-%d-%H%M")


# model name used for saving the model
modelname = grid + "_" +model + "_" + str(Epochs) + "_" + str(nodes) + "_" + str(eta) + "_" + str(lamda) + "_" + timestamp
print(modelname)

# load the dataset used for the neural network, made from read-data.py with the HiggsML dataset
df = pd.read_csv("../data/data_" + model + ".csv")

# extract the label fearure
labels = df.pop('Label')

# split the data into training and testing
train, test, train_label, test_label = train_test_split(df, labels, test_size=0.2, train_size=0.8, random_state=9)

# convert the data into numpy array for faster computation
train = np.array(train)
test = np.array(test)
train_label = np.array(train_label)
test_label = np.array(test_label)

model = NeuralNetwork(df.shape[1], nodes, eta, lamda, train, train_label, 'binary_crossentropy')
# model = NeuralNetwork(df.shape[1], nodes, eta, lamda, train, train_label, 'custum_binary_crossentropy')

# load the history of the model
history = model.fit(train, train_label,
                   validation_data=(test, test_label),
                   batch_size=10000, 
                    epochs=Epochs,)


# output from the model
y_pred_keras = model.predict(test).ravel()

# convert the output to the likelihood ratio
likelihood_ratio = y_pred_keras/(1-y_pred_keras)

# make the ROC curve
fpr_keras, tpr_keras, thresholds_keras = roc_curve(test_label, y_pred_keras)

y_pred = np.round(y_pred_keras).tolist()

# calculate the auc from the ROC curve
auc_keras = auc(fpr_keras, tpr_keras)


# load the variables from the history
loss = np.array(history.history['loss'])
val_loss = np.array(history.history['val_loss'])
auc = np.array(history.history['auc'])
val_auc = np.array(history.history['val_auc'])
accuracy = np.array(history.history['accuracy'])
val_accuracy = np.array(history.history['val_accuracy'])

# convert the variables to numpy arrays
fpr = np.array(fpr_keras)
tpr = np.array(tpr_keras)
auc_end = np.array(auc_keras)
y_true = np.array(test_label)
y_pred = np.array(y_pred_keras)
likelihood_ratio = np.array(likelihood_ratio)


# save the variables to a file used for plotting (see plotting.py)
np.savez("../plots/raw/"+modelname+".npz", loss=loss, val_loss=val_loss, accuracy=accuracy, val_accuracy=val_accuracy, fpr=fpr, tpr=tpr, auc_end=auc_end, auc=auc, val_auc=val_auc, y_true=y_true, y_pred=y_pred, likelihood_ratio=likelihood_ratio)
