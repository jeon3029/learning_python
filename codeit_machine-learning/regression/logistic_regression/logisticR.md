# 로지스틱 회귀(Logistic Regression)

- 분류문제
- 선형회귀로도 로지스틱 회귀(분류)를 할 수 있으나 이상점(특이한 데이터)로인해 회귀선의 기울기값이 크게 조정될 수 있어서 잘 쓰이지 않음
- ![image1](image/img1.PNG)

## 로지스틱 회귀

- 선형회귀 : 예외적인 데이터에 민감하다 --> 로지스틱 회귀의 시그모이드 함수 사용
  
### 시그모이드 함수

- ![exp1](https://latex.codecogs.com/gif.latex?S%28x%29%20%3D%20%5Cfrac%7B1%7D%7B1&plus;e%5E%7B-x%7D%7D)
- ![image2](image/img2.PNG)
  - 항상 0~1사이의 값

## 로지스틱 회귀 가설함수

- ![exp2](https://latex.codecogs.com/gif.latex?g_%5Ctheta%28x%29%20%3D%20%5Ctheta%5E%7BT%7Dx)
- ![exp3](https://latex.codecogs.com/gif.latex?h_%5Ctheta%28x%29%20%3D%20%5Cfrac%7B1%7D%7B1&plus;e%5E%7B-g_%5Ctheta%28x%29%7D%7D%20%3D%20%5Cfrac%7B1%7D%7B1&plus;e%5E%7B-%5Ctheta%5E%7BT%7Dx%7D%7D)
  - 나온값은 항상 0~1사이의 값 : 1에가까울 수록 통과(분류) 될 확률이 높음
- ![image3](image/img3.PNG)
- 변수가 여러개 일때는 시각화 하기는 어렵지만, 똑같이 생각하면 됨
- ![image4](image/img4.PNG)

## 로지스틱 회귀 손실함수

- 로그 손실
  - ![image5](image/img5.PNG)
    - 손실의 정도를 로그함수(log-loss)로 결정!
  - ![image6](image/img6.PNG)
    - 한 줄로 표현
- 손실 함수
  - ![image7](image/img7.PNG)
  - ![image8](image/img8.PNG)

## 로지스틱 회귀 경사하강법

- 편미분 해서 손실함수를 통해 경사하강법 실시
  - 선형회귀와 같은 결과가 나옴(과정 생략)
- ![image9](image/img9.PNG)
  - j : 1~n
- ![exp4](https://latex.codecogs.com/gif.latex?%5Ctheta%20%5Cleftarrow%20%5Ctheta-%5Calpha%5Cfrac%7B1%7D%7Bm%7D%28X%5E%7BT%7D*%20error%29)

## 분류가 3개 이상일 때

- ![image10](image/img10.PNG)
- 가장 높은 값으로 예측

## 정규 방정식

- 선형 회귀처럼 단순 행렬 연산만으로 최소지점 찾을 수 없음
  - 로지스틱회귀의 손실함수는 convex형태임
  - 하지만, 편미분한 형태는 convex형태가 아님


## sklearn

- sklearn.ipynb참고