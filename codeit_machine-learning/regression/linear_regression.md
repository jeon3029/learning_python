## 선형회귀
- 집가격 예측 모델   
![image1](image/img1.PNG)
- 가장 데이터셋을 잘 표현하는 직선을 찾는 것

## 선형회귀 용어
- 지도학습이라고 할 수 있음 (회귀)
- 목표변수 : target variable/output variable
- 입력변수 : input variable/feature
- 학습데이터의 갯수 : M
    - 1번 인풋데이터의 값 = 1번 아웃풋 데이터
    - ![exp1](https://latex.codecogs.com/gif.latex?x%5E%7B%281%29%7D%20%3D%20y%5E%7B%281%29%7D)


## 가설함수
- 선형함수로 표현
- ![exp2](https://latex.codecogs.com/gif.latex?h%28x%29%20%3D%20%5CTheta_0%20&plus;%20%5CTheta_x)
- 변수가 많아지면 x1, x2, ...
- ![exp3](https://latex.codecogs.com/gif.latex?h_%5CTheta%28x%29%20%3D%20%5CTheta_0%20&plus;%20%5CTheta_1x_1%20&plus;%20%5CTheta_2x_2%20&plus;...)
- 가장 적절한 theta 를 찾아낸다.

## 평균제곱오차(MSE)
- 가설함수 평가방법 중 하나
- ![image2](image/img2.PNG)
- 차이의 제곱을 평균낸다

## 평균제곱오차 일반화
- ![exp4](https://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29%20-%20y%5E%7B%28i%29%7D%29%5E%7B2%7D)