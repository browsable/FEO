import h2checker, logging,scraping
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
#url = 'http://www.facebook.com/'-문제아
#url = 'somacon.kr'
url = 'nghttp2.org'
h2AndUrl = h2checker.excuteCheckFunc(url) # return (H2Support,Url)
h2support = h2AndUrl[0]
url_redirect = h2AndUrl[1]

if(h2support):
    scraping.resDownload(url_redirect)
# else:
#     logger.info('This domain dose not supports HTTP/2')



# h2support = h2checker_not_redirect.excuteCheckFunc(url)
#
# if(h2support):
#     logger.info('This domain supports HTTP/2')
# else:
#     logger.info('This domain dose not supports HTTP/2')