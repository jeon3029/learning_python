from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pandas as pd

# 데이터 셋 불러 오기
cancer_data = load_breast_cancer()
# 데이터 셋을 살펴보기 위한 코드
# print(cancer_data.DESCR)

X = pd.DataFrame(cancer_data.data,columns=cancer_data.feature_names)
# print(X)
y = pd.DataFrame(cancer_data.target,columns=['clas'])
# print(y)
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 5)
y_train = y_train.values.ravel()
# 출력 코드
model = RandomForestClassifier(n_estimators=10,max_depth=4,random_state=42)
model.fit(x_train,y_train)
predictions = model.predict(x_test)
score = model.score(x_test,y_test)

print(predictions, score)