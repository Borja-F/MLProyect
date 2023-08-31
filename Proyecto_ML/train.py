# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L5LH2GzVBnwLGxX3yih6ZYeG300FqWx5
"""

import numpy as np
import pandas as pd
import seaborn as sns
import ast

from keras.layers import Conv1D, GlobalMaxPooling1D

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import pickle
# Load libraries
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
# TensorFlow y tf.keras
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import classification_report, confusion_matrix


from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV

from tensorflow.keras.layers import Dense, Conv2D, Flatten, Activation, Dropout, MaxPooling2D
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam
# Set random seed
np.random.seed(42)
from tensorflow.keras.optimizers import Adam

from google.colab import files
uploaded = files.upload()

df4 = pd.read_csv("/content/drive/MyDrive/Copia de Datos_opt.csv",index_col=0)

replace_dict = {'popular': 0, 'normal': 1, 'impopular': 2}

df4["label"] = df4["label"].replace(replace_dict)



X = df4.drop('label', axis=1)
y = df4['label']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size = 0.20,
                                                    random_state=42)

X_train.shape

X_train.info()

model = keras.models.Sequential()

model.add(keras.layers.Dense(input_shape=(804,), units=512, activation="relu"))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Dropout(0.2))

model.add(keras.layers.Dense(256))
model.add(keras.layers.LeakyReLU(alpha=0.1))
model.add(keras.layers.Dropout(0.2))

model.add(keras.layers.Dense(128))
model.add(keras.layers.PReLU())
model.add(keras.layers.Dropout(0.3))

model.add(keras.layers.Dense(64))
model.add(keras.layers.ELU(alpha=1.0))
model.add(keras.layers.Dropout(0.3))

model.add(keras.layers.Dense(32, activation="relu"))
model.add(keras.layers.Dropout(0.3))

model.add(keras.layers.Dense(units=3, activation='softmax'))

model.compile(
    optimizer = Adam(learning_rate=0.00001),
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"])

early_stopping_cb = keras.callbacks.EarlyStopping(patience=10)
checkpoint_cb = keras.callbacks.ModelCheckpoint("callback_raro.h5",
                                                save_best_only=True)

history = model.fit(X_train,
                    y_train,
                    epochs=1000,
                    batch_size=128,
                    validation_split=0.2,
                    callbacks = [early_stopping_cb, checkpoint_cb])

predictions2 = model.predict(X_test)

predictions2

predictions

test_loss, test_acc =  model.evaluate(X_test,y_test)

predictions = np.argmax(model.predict(X_test), axis=1)

confusion_matrix(y_test, predictions)