# -*- coding: utf-8 -*-
"""
@author: Erick Gildardo Avalos Soiis
"""

from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import numpy as np
from tensorflow import keras
def crear_sistema_inteligente(n,nv,nn,ni,X,Y):
    
    print(X)
    X=np.asarray(X)
    print(X)
    X=np.array(X)
    #print(X)
    print(Y)
    print(nv)
    print(nn)
    print(ni)
    model = Sequential()
    model.add(Dense(12, input_dim=nv, activation='relu'))
    model.add(Dense(nn, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])
    model.fit(X, Y, epochs=ni)
    
    predictions = model.predict(X)
    
    model.save('%s.h5'% n)

def usar_ia(X,N):
    new_model = keras.models.load_model('%s.h5'% N)
    predictions = new_model.predict(X)
    Y = [round(x[0]) for x in predictions]
    return Y