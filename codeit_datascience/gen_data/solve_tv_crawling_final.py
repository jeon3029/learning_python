import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

records = []


response = requests.get("https://workey.codeit.kr/ratings/index")
soup = BeautifulSoup(response.text, 'html.parser')
divs = soup.select('.row')
records = []
period = soup.select("#weekSelectBox option")[0].text

init = 0
for row in divs:
    # print(row.find(class_='rank').text)
    if init==0:
        init+=1
        continue
    record=[]
    rank = row.find(class_='rank').text
    channel = row.find(class_='channel').text
    program = row.find(class_='program').text
    rating = row.find(class_='percent').text
    record.append(period)
    record.append(rank)
    record.append(channel)
    record.append(program)
    record.append(rating)
    records.append(record)
# # DataFrame 만들기
df = pd.DataFrame(data=records, columns=["period", "rank", "channel","program","rating"])
df.head()
# # DataFrame 출력
# df.head()
