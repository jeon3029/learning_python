
## Parsing 1
- 파이썬에서는 Beautiful Soup이라는 툴로 HTML을 파싱
```python
html_code ="""<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습!</h2>

<p>이것은 첫 번째 문단입니다.</p>
<p>이것은 두 번째 문단입니다!</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')
print(type(soup)) # <class 'bs4.BeautifulSoup'>

li_tags = soup.select('li') # 모든 li태그 선택
print(li_tags) # [<li>커피</li>, <li>녹차</li>, <li>우유</li>]
print(li_tags[0]) #<li>커피</li>
print(li_tags[0].text) #커피

for li in li_tags:
    beverage_names.append(li.text)
print(beverage_names) #['커피', '녹차', '우유']
```

## Parsing 2
- 태그의 속성값 추출 사용법
```python
from bs4 import BeautifulSoup

html_code = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습!</h2>

<p>이것은 첫 번째 문단입니다.</p>
<p>이것은 두 번째 문단입니다!</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>"""

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(html_code, 'html.parser')

# 모든 <img> 태그 선택하기
img_tags = soup.select('img')

# 결과 출력
print(img_tags) #[<img alt="coffee" src="https://i.imgur.com/bY0l0PC.jpg"/>, <img alt="green-tea" src="https://i.imgur.com/fvJLWdV.jpg"/>, <img alt="milk" src="https://i.imgur.com/rNOIbNt.jpg"/>]

#1번째 항목만 선택
print(img_tags[0]) #<img alt="coffee" src="https://i.imgur.com/bY0l0PC.jpg"/>

# 첫 번째 요소의 "src" 속성 값 가져오기 예제
print(img_tags[0]["src"]) #https://i.imgur.com/bY0l0PC.jpg

# 빈 리스트에 모든 이미지 주소 넣기!
img_srcs = []

# 이미지 주소 추출해서 리스트에 담기
for img in img_tags:
    img_srcs.append(img["src"])
```


## Parsing 3
- 실제 사이트 크롤링 예제
```python
import requests

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# <h3 class="popular__title">인기 아티스트</h3> 항목 있음 데이터 추출
li_tags = soup.select(".popular__order li")
# 빈 리스트 생성
popular_artists = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    popular_artists.append(li.text.strip())# 공백 제거

print(popular_artists)
#['1 아이유 (IU)', '2 방탄소년단', '3 Red Velvet (레드벨벳)', '4 IKON', '5 멜로망스', '6 다비치', '7 윤딴딴', '8 수지 (SUZY)', '9 김동률', '10 폴킴']

```

