import h2checker, logging,scraping
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
#url = 'http://www.facebook.com/'
url = 'https://www.somacon.kr/'
H2AndUrl = h2checker.excuteCheckFunc(url)
print(list)
if(H2AndUrl[0]):
    scraping.resDownload(H2AndUrl[1])

# h2support = h2checker_redirect.excuteCheckFunc(url)
#
# if(h2support):
#     logger.info('This domain supports HTTP/2')
# else:
#     logger.info('This domain dose not supports HTTP/2')