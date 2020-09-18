import requests
from bs4 import BeautifulSoup

rating_pages = []
for year in range(2010,2019):
    for month in range(1,13):
        for week in range(0,5):
            response = requests.get('https://workey.codeit.kr/ratings/index?year='+str(year)+'&month='+str(month)+'&weekIndex='+str(week))
            soup = BeautifulSoup(response.text, 'html.parser')
            if len(soup.select('.row .rank')) == 1:
                break
            else:
                rating_pages.append(response.text)

# response = requests.get('https://workey.codeit.kr/ratings/index?year=2010&month=2&weekIndex=3')
# soup = BeautifulSoup(response.text, 'html.parser')
# print(len(soup.select('.row .rank')))
print(len(rating_pages))  # 가져온 총 페이지 수
print(rating_pages[0])  # 첫 번째 페이지의 HTML 코드

