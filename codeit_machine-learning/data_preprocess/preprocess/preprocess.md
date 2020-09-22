# 데이터 전처리

- 데이터를 그대로 사용하지 않고 가공하여 모델을 학습시키는 데 좋은 형식으로 만들어 줌

## Feature Scaling

- 입력 변수의 크기 조정해서 일정 범위 내에 떨어지도록 함
- ![image1](image/img1.PNG)
- 경사하강법을 좀 더 빨리할 수 있게 도와줌

### min-max normalization

- 0 ~ 1사이값으로 만드는 것
- ![exp1](https://latex.codecogs.com/gif.latex?x_%7Bnew%7D%20%3D%20%5Cfrac%7Bx_%7Bold%7D-x_%7Bmin%7D%7D%7Bx_%7Bmax%7D-x_%7Bmin%7D%7D)

### sklearn - feature scaling

- sklearn.ipynb 참고
