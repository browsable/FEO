import requests,os,logging,urllib.request
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)

def getSrcPath(src, url, originPath):
    src = str(src)
    if("http" not in src):
        src = src[src.find("src=\"")+5:]
        src = src[:src.find("\"")]
        src = src.replace("../","/")
        logger.info(src)
        srcPath = src[:src.rfind("/")]
        makeDirectory(originPath +"/"+srcPath)
        resource = requests.get(url+"/"+src).content
        with open(originPath+"/"+src, "wb") as code:
             code.write(resource)

def getHrefPath(href, url, originPath):
    href = str(href)
    if ("http" not in href):
        href = href[href.find("href=\"")+6:]
        href = href[:href.find("\"")]
        href = href.replace("../", "/")
        logger.info(href)
        hrefPath = href[:href.rfind("/")]
        makeDirectory(originPath + "/" + hrefPath)
        resource = requests.get(url + "/" + href).content
        with open(originPath + "/" + href, "wb") as code:
            code.write(resource)

def makeDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def resDownload(url): #img, js, css
    logger.info('*********** Resource Download Start ***********')
    html = requests.get(url).content
    originPath = url + '/origin/';  # 사이트 원본 Path
    optPath = url + '/opt/'  # 사이트 최적화 Path
    makeDirectory(originPath)
    # makeDirectory(optPath)
    soup = BeautifulSoup(html, 'lxml')
    # html
    with open(originPath + "index.html", "wb") as code:
        code.write(html)
    # image
    imgs = soup.findAll('img', {"src": True})
    for img in imgs:
        getSrcPath(img, url, originPath)
    # .js
    scripts = soup.findAll('script', {"src": True})
    for script in scripts:
        getSrcPath(script, url, originPath)
    # .css
    stylesheets = soup.findAll('link', {"type": "text/css", "href": True})
    for stylesheet in stylesheets:
        getHrefPath(stylesheet, url, originPath)
    logger.info('*********** Resource Download End ***********')
