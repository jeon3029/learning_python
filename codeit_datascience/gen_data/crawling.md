## 필요한 페이지만 가져오기
- 페이지가 없는 경우를 구분하여 가져와야함
- 연속적으로 페이지 접근하면 차단하는 경우도 있으므로 time.sleep(3) 등을 걸어주면 좋음
```python
import time
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
pages = []

# 첫 페이지 번호 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))

    # BeautifulSoup 타입으로 변환하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # ".csrch_tip" 클래스가 없을 때만 HTML 코드를 리스트에 담기
    if len(soup.select('.csrch_tip')) == 0:
        pages.append(soup)
        print(str(page_num) + "번째 페이지 가져오기 완료")
        page_num += 1
        time.sleep(3)
    else:
        break

# 가져온 페이지 개수 출력하기
print(len(pages))
```