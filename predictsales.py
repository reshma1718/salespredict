import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

dataset = pd.read_csv('multipleregression.csv')

X = dataset.iloc[:, :3]
Y = dataset.iloc[:,-1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, Y)

pickle.dump(regressor, open('predictsales.pkl','wb'))

model = pickle.load(open('predictsales.pkl','rb'))
print(model.predict([[10, 43, 10]]))