import numpy as np 
from sklearn.neural_network import MLPClassifier  
import pickle
# Model persistence
output_model_file = 'annmodel.pkl'

# Load the model
with open(output_model_file, 'rb') as f:
    mlp = pickle.load(f)
    
import pandas as pd  
# dataset = pd.read_csv("./data/irisTestSet.csv")
# Preprocessing
#X = dataset.iloc[:, 1:5]  
#y = dataset.iloc[:, 5]
X = np.array([[112.3471467,0.078929391,0.050747461,-152.3824629,90.17857392,0.272525009,0.157586409,2566.309357,1047.229413,24.03077208,7.126945819,5408.462488,2160.759494]])

print(X)

from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
scaler.fit(X)
X = scaler.transform(X)

# from sklearn import preprocessing  
# le = preprocessing.LabelEncoder() 
# le.fit(y)
# # Print the mapping
# print("\nLabel mapping:")
# for i, item in enumerate(le.classes_):
#     print(item, '-->', i)
# y = le.transform(y)


predictions = mlp.predict(X)
print(predictions)
# from sklearn.metrics import classification_report, confusion_matrix
# print(confusion_matrix(y,predictions))  
# print(classification_report(y,predictions))  
