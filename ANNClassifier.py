# Importing Libraries
import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  

# Importing the Dataset
# Assign column names to the dataset
# attribute_names = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
# dataset = pd.read_csv("./data/iris.csv", names = attribute_names)
dataset = pd.read_csv("/Users/dippaul/Desktop/MUSIC_FEATURE_EXTRACTION/Datsset/music_mood.csv")
from sklearn import preprocessing  
le = preprocessing.LabelEncoder() 
le.fit(dataset['Emotion'])
dataset['Emotion'] = le.transform(dataset['Emotion'])
# Print the mapping
print("\nLabel mapping:")
for i, item in enumerate(le.classes_):
    print(item, '-->', i)


# Preprocessing
X = dataset[['Tempo','ZCR Mean','ZCR Std Dev','MFCC Mean','MFCC Std Dev','CEN Mean','CEN Std Dev','CENTROID Mean','CENTROID Std Dev','Contrast Mean','Contrast Std Dev','Rolloff Mean','Rolloff Std Dev']]
#X = dataset[['Tempo','ZCR Mean','ZCR Std Dev','MFCC Mean','MFCC Std Dev']]
#X = dataset[['Tempo','ZCR Mean','ZCR Std Dev','MFCC Mean','MFCC Std Dev','CEN Mean','CEN Std Dev','CENTROID Mean','CENTROID Std Dev']]
y = dataset[['Emotion']]
print(X.head()) 
print(y.head())

#print(y.unique())


from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
scaler.fit(X_train)
  
X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)  
print("X_train Size: ", len(X_train), " and X_test Size: ",  len(X_test))

from sklearn.neural_network import MLPClassifier  
mlp = MLPClassifier(hidden_layer_sizes=(10), max_iter=10000)
#mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)
#mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)  
mlp.fit(X_train, y_train)  

predictions = mlp.predict(X_test)  

from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,predictions))  
print(classification_report(y_test,predictions))  

import pickle
# Model persistence
output_model_file = 'annmodel.pkl'

# Save the model
with open(output_model_file, 'wb') as f:
    pickle.dump(mlp, f)

