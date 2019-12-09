from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd
import numpy as np
import os
import pandas.plotting as pdl

#dont worry about this method, its for the other methods
def uni(dataset, start, end, history, target): 
    things = []
    titles = []

    start = start + history
    if end is None:
        end = len(dataset) - target
    for i in range(start, end):
        indices = range(i-history, i)
        things.append(np.reshape(dataset[indices], (history, 1)))
        titles.append(dataset[i+target])
    return np.array(things), np.array(titles)
#this dataset opens the csv file and returns a dataset. Feed it csv file name
def dataset(csv):
	
    df = pd.read_csv(csv)
    print("Read csv")
    df['number'] = np.arange(len(df))
    datau = df["number"]
    datau.index = df["time"]
    datau = datau.values
    datau_mean = datau.mean()
    datau_std = datau.std()
    datau = (datau-datau_mean)/datau_std
    return datau;
#formats the dataset and returns a list of stuff. Feed it dataset from dataset method above
def dataformat(dataset):

    x_val, y_val = uni(dataset, 0, None, 50, 0)

    validate = tf.data.Dataset.from_tensor_slices((x_val, y_val))
    validate = validate.batch(528).repeat()
    return [x_val, y_val, validate]
#retrives the model. Feed it model name, it returns model. Usage: ai = model('modelname.h5')
def model(modfile):
    model = tf.keras.models.load_model(modfile)
    return model
#returns numpy array of prediction. feed it model and one of the items from the dataformat list
def predict(data, model):
    mod = model
    results = mod.predict(data)
    return results
