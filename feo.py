import h2checker, logging,coloredlogs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
#url = 'http://www.facebook.com/'
url = 'https://www.somacon.kr/'
h2support = h2checker.excuteCheckFunc(url)

if(h2support):
    logger.info('This domain supports HTTP/2')
else:
    logger.info('This domain dose not supports HTTP/2')