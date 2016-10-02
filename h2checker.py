import requests,alpnchecker


def excuteCheckFunc(url):
	if url.startswith('https://'):
		return checkH2S(url)
	elif url.startswith('http://'):
		return checkH2(url)

def checkH2S (url):
	return alpnchecker.alpnChecker(url)

def checkH2 (url):
	headers = {'Accept': '*/*', 'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4','user-agent': 'my-app/0.0.1', 'Connection': 'Upgrade, HTTP2-Settings', 'Upgrade': 'h2c',
			   'HTTP2-Settings': '<base64url encoding of HTTP/2 SETTINGS payload>'}
	r = requests.get(url, headers=headers, allow_redirects=False)
	#Check HTTP
	if r.status_code == 101:
		return alpnchecker.alpnChecker(url)
	elif r.status_code == 301 or r.status_code == 302:
		location =  r.headers['Location']
		if (location.startswith("http")):
			url = location
		else:
			url = url + "/" + location
		return excuteCheckFunc(url)
	else:
		print('HOST is ' + url)
		return False
