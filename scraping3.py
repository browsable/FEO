import urllib, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def spider(url):
    headers = {'Accept': '*/*', 'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4', 'user-agent': 'my-app/0.0.1',
               'Connection': 'Upgrade, HTTP2-Settings', 'Upgrade': 'h2c',
               'HTTP2-Settings': '<base64url encoding of HTTP/2 SETTINGS payload>'}
    source_code = requests.get(url, headers=headers, allow_redirects=False)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    imgs = soup.findAll('img')
    for img in imgs:
        print(img)
    print(len(imgs))

spider('http://www.naver.com')