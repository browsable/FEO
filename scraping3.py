from bs4 import BeautifulSoup
import urllib.request
import re
import requests

url = "http://www.naver.com"
r = requests.get(url)
html_content = r.text

soup = BeautifulSoup(html_content,"html.parser")

imgs = soup.find_all('img')


# for img in imgs:
#     print(img)

links = soup.find_all('link')

for link in links:
    requests.get(url)
    html_content = r.text


#print(len(soup.find_all('img')))