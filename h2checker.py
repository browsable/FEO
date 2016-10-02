import requests,alpnchecker


def excuteCheckFunc(url):
	if url.startswith('https://'):
		checkH2S(url)
	elif url.startswith('http://'):
		checkH2(url)

def checkH2S (url):
	return alpnchecker.alpnChecker(url)

def checkH2 (url):
	headers = {'Accept': '*/*', 'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4','user-agent': 'my-app/0.0.1', 'Connection': 'Upgrade, HTTP2-Settings', 'Upgrade': 'h2c',
			   'HTTP2-Settings': '<base64url encoding of HTTP/2 SETTINGS payload>'}
	r = requests.get(url, headers=headers, allow_redirects=False)
	#Check HTTP
	if r.status_code == 101:
		print ('This domain supports HTTP/2')
		return alpnchecker.alpnChecker(url)
	elif r.status_code == 301 or r.status_code == 302:
		location =  r.headers['Location']
		if (location.startswith("http")):
			url = location
		else:
			url = url + "/" + location
		excuteCheckFunc(url)
	else:
		print ('This domain does not support HTTP/2 with h2c')
		print (r.status_code);
		print(alpnchecker.alpnChecker(url))
		return alpnchecker.alpnChecker(url)
