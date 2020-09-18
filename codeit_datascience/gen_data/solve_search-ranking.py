import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

divs = soup.select('.rank__order .list')
# print (divs)
parsed = []
for ele in divs:
    parsed.append(ele.text.strip().split()[2])
print(parsed)
