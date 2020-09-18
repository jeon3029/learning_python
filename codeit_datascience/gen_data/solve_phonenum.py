import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

divs = soup.select('.container .branch .phoneNum')
# print (divs)
parsed = []
for ele in divs:
    parsed.append(ele.text)
print(parsed)
