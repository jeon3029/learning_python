# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd  

diabetes_dataset = datasets.load_diabetes()  # 데이터 셋 갖고오기


# 문제1
poly_trans = PolynomialFeatures(2)
poly_data = poly_trans.fit_transform(diabetes_dataset.data)
poly_feature = poly_trans.get_feature_names(diabetes_dataset.feature_names)
# print(poly_feature)
X = pd.DataFrame(poly_data,columns=poly_feature)

# print(X.head())

# 문제 2

# 목표 변수
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=5)
model = LinearRegression()
model.fit(x_train,y_train)
y_test_predict = model.predict(x_test)
mse = mean_squared_error(y_test, y_test_predict)
print(mse ** 0.5)