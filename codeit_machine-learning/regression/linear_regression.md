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

> ![exp4](https://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29%20-%20y%5E%7B%28i%29%7D%29%5E%7B2%7D)

## 손실함수

- 가설함수의 성능을 평가하는 함수
- 손실함수가 작으면 : 가설함수가 데이터에 잘 맞다
- 손실함수가 크면 : 가설함수가 데이터에 잘 안맞다
- MSE의 손실함수 
  > ![exp5](https://latex.codecogs.com/gif.latex?%5Ciota%28%5Ctheta%29%20%3D%20%5Cfrac%7B1%7D%7B2m%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-%20y%5E%7B%28i%29%7D%29%5E%7B2%7D)
  - input이 Theta 임(이 theta를 조정해서 효율적인 theta를 찾음)
  - theta = theta0,theta1, ... 를 하나로 묶어서 쓴것

## 경사 하강법(Gradient Descent)

- Theta값을 바꿔 손실함수의 아웃풋을 최소화 하는 기법 중 하나
- Theta 값을 통해 기울기를 측정하고 그 기울기에 따라 극소점을 찾아나감
- Theta input 2개 인 경우
  - 편미분해서 방향을 찾음
  - ![image3](image/img3.png)
  - '-' 를 붙이면 내려가는 방향!

### 경사하강법 테크닉

- Theta = Theta0, Theta1 인 경우, 편미분해서 기울기함수를 구해줌
- ![image4](image/img4.png)
- 학습률 alpha를 곱해서 현재 위치에서 빼줌(alpha 는 얼마나 내려가는지 계수를 의미)
- ![exp6](https://latex.codecogs.com/gif.latex?new%5C%20%5C%20%5Ctheta_0%20%3D%20-3%20-%20%5Calpha%20*%20%28-6%29)
- 일반화 : ![image5](image/img5.png)
  - 각 Theta에 대해 편미분한 결과를 alpha를 곱해서 빼줌
- Theta updata 일반화 공식
  - ![image6](image/img6.png)
