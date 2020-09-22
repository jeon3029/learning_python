# 다중 선형 회귀

- 입력 변수가 두개이상인 상황
- 시각화는 힘들지만 기본 개념은 같음

## 다중 선형회귀 표현법

- ![image1](image/img1.PNG)
- 입력 변수 여러개 : feature 여러개
- 목표변수는 여전히 1개
- i번째 데이터 j번째 속성 : ![exp1](https://latex.codecogs.com/gif.latex?x_j%20%5E%7B%28i%29%7D)

## 다중 선형 회귀 가설 함수

- ![exp2](https://latex.codecogs.com/gif.latex?h_%5CTheta%28x%29%20%3D%20%5CTheta_0%20&plus;%20%5CTheta_1x_1%20&plus;%20%5CTheta_2x_2%20&plus;...)
- 각 theta는 feature
- theta 를 조율하여 최적의 값 구하기
- ![image2](image/img2.PNG)
- 가설함수를 간단하게 표현한 것

## 다중 선형 회귀 경사 하강법

- 손실함수
  
 > ![exp3](https://latex.codecogs.com/gif.latex?%5Ciota%28%5Ctheta%29%20%3D%20%5Cfrac%7B1%7D%7B2m%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-%20y%5E%7B%28i%29%7D%29%5E%7B2%7D)

- 손실함수의 값이 작으면 --> 데이터에 잘 맞다
- 경사하강법(j : 1부터 n까지)
  - ![image3](image/img3.PNG)

## 다중 선형 회귀 쉽게 표현하기

- 모든 데이터 예측값
  - ![image4](image/img4.PNG)
  - x0 = 1
- 예측 오차
  - ![image5](image/img5.PNG)
- 경사하강법
  - ![image7](image/img7.PNG)
    - 유도과정
  - ![image6](image/img6.PNG)

## 정규방정식

- 손실함수

> ![exp5](https://latex.codecogs.com/gif.latex?%5Ciota%28%5Ctheta%29%20%3D%20%5Cfrac%7B1%7D%7B2m%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x%5E%7B%28i%29%7D%29-%20y%5E%7B%28i%29%7D%29%5E%7B2%7D)

- ![exp4](https://latex.codecogs.com/gif.latex?%5Ctriangledown%20%5Ciota%20%28%5Ctheta%29%20%3D%200)
  - 손실함수를 미분해서 0되는 지점 찾기
- ![image8](image/img8.PNG)

### 경사하강법 vs 정규 방정식 비교

- ![image9](image/img9.PNG)

## Convex함수

- 아래로 볼록한 함수
  - 경사하강법을 사요했을 때 극소점이 하나만 나오는 형태
  - Convex 형태가 아니라면, 구한 극소점이 최소점이 아닐 수 있음

## Scikit-learn

- sklearn.ipynb 참고