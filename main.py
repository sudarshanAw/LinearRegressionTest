#importing libraries
import pandas as pnd
from sklearn.model_selection import train_test_split
import joblib


#importing dataset
dataset = pnd.read_csv('data/Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values


#splitting into training and test sets
X_train,X_Test,y_train,y_test = train_test_split(X,y,test_size=0.15,shuffle=True,random_state=42);

#creating a linear regressor
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train,y_train)

results = regressor.predict([[5.5]])

print(results[0])

filename = 'linear_model.pkl'
joblib.dump(regressor,filename)