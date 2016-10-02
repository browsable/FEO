import h2checker,alpnchecker

url = 'https://www.naver.com'
#url = 'http://www.facebook.com'
h2support = h2checker.excuteCheckFunc(url)
if(h2support):
    print('This domain supports HTTP/2')
else:
    print('This domain dose not supports HTTP/2')