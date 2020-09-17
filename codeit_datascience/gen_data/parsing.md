
## 파싱1
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

## 파싱2
