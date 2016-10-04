import h2checker, logging,scraping
logging.basicConfig(level=logging.DEBUG)
#url = 'http://www.facebook.com/'-문제아
url = 'nghttp2.org'

# h2 support checking
h2checker.checkH2(url)
h2checker.checkH2S(url)

#scraping
scraping.resDownload(url)