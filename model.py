import numpy as np
from tensorflow import keras
from keras import models
from keras.layers import Dense
import csv

# Model / data parameters
num_classes = 2 
num_features = 17

def prepare_data():
  x_train = []
  y_train = []
  x_test = []
  y_test = []
  total_samples = 20000
  training_samples = total_samples * 0.8

  # load the data from the csv
  with open('clean_heart.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    positive_count = 0
    negative_count = 0
    for row in csv_reader:
      if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
      elif negative_count == total_samples/2 and int(row[0]) == 0:
        continue 
      elif positive_count == total_samples/2 and int(row[0]) == 1:
        continue
      elif line_count < training_samples:
        converted_row = [float(string) for string in row]
        x_train.append(converted_row[1:])
        arr = np.zeros(num_classes)
        arr[int(row[0])] = 1
        y_train.append(arr)
        if int(row[0]) == 0:
          negative_count += 1
        else:
          positive_count += 1
        line_count += 1
      elif line_count < total_samples:
        converted_row = [float(string) for string in row]
        x_test.append(converted_row[1:])
        arr = np.zeros(num_classes)
        arr[int(row[0])] = 1
        y_test.append(arr)   
        if int(row[0]) == 0:
          negative_count += 1
        else:
          positive_count += 1     
        line_count += 1
    print(f'Processed {line_count} lines.')

  # convert to numpy arrays
  x_train = np.asarray(x_train)
  y_train = np.asarray(y_train)
  x_test = np.asarray(x_test)
  y_test = np.asarray(y_test)

  # Scale vectors to the [0, 1] range
  x_train = x_train.astype("float32") / 120
  x_test = x_test.astype("float32") / 120

  print("x_train shape:", x_train.shape)
  print("y_train shape:", y_train.shape)
  print(x_train.shape[0], "train samples")
  print(x_test.shape[0], "test samples")

  return x_train, y_train, x_test, y_test

def train_model(x_train, y_train, x_test, y_test):
  model = models.Sequential()
  #model.add(Dense(num_classes, activation='sigmoid', input_shape=(num_features,)))
  model.add(Dense(20, activation='relu', input_shape=(num_features,)))
  model.add(Dense(num_classes, activation='sigmoid'))
  model.summary()

  batch_size = 128
  epochs = 15
  model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-2), loss="categorical_crossentropy", metrics=["accuracy"])
  model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
  score = model.evaluate(x_test, y_test, verbose=0)
  print("Test loss:", score[0])
  print("Test accuracy:", score[1])

if __name__ == '__main__':
  x_train, y_train, x_test, y_test = prepare_data()
  train_model(x_train, y_train, x_test, y_test)
