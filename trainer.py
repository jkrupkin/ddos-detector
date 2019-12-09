import tensorflow as tf
import pandas as pd
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow.keras import layers
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


train_split = 4698930
#train_data = tf.data.experimental.make_csv_dataset("target.csv", batch_size=100)

print("hello")

df = pd.read_csv("xaa.csv", usecols = [2], engine="python")
print("hello2")
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.hour * 60 + df['time'].dt.minute + df['time'].dt.second/60

df['number'] = np.arange(len(df))
datau = df["number"]
datau.index = df["time"]
#datau.head()

datau = datau.values
datau_mean = datau[:train_split].mean()
datau_std = datau[:train_split].std()
#tf.enable_eager_execution()
datau = (datau-datau_mean)/datau_std
x_train, y_train = uni(datau, 0, train_split, 50, 0)
x_val, y_val = uni(datau, train_split, None, 50, 0)
#model production"
batch_size = 256
buffer_size = 2000
trainer = tf.data.Dataset.from_tensor_slices((x_train, y_train))
#trainer = trainer.cache().shuffle(1000).batch(528)
validate = tf.data.Dataset.from_tensor_slices((x_val, y_val))
#validate = validate.batch(528).repeat()
model = tf.keras.Sequential()

#model.add(preprocessing_layer)
model.add(layers.LSTM(256, input_shape=x_train.shape[-2:]))
model.add(layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='mae', metrics=['accuracy'])
model.fit(trainer, epochs=200, steps_per_epoch = 200, validation_data=validate, validation_steps=50)
model.summary()
#tf.saved_model.save(model, "Enter filename here") #Enter filename to save model
