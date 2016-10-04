import requests,os,logging
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)

def resDownload(url): #img, js, css
    logger.info('*********** Resource Download Start ***********')

    r = requests.get("http://"+url,allow_redirects=True)
    urlRedirect = r.url

    originPath = 'origin/'+ urlRedirect;  # 사이트 원본 Path
    #optPath = 'opt/' + url_redirect # 사이트 최적화 Path\

    html = r.content
    soup = BeautifulSoup(html, 'lxml')

    # image
    imgs = soup.findAll('img', {"src": True})
    for imgURL in imgs:
        getSrcPath(urlRedirect, imgURL, originPath, "img")

    # .js
    scripts = soup.findAll('script', {"src": True})
    for scriptURL in scripts:
        getSrcPath(urlRedirect, scriptURL, originPath, "js")

    # .css
    stylesheets = soup.findAll('link', {"type": "text/css", "href": True})
    for stylesheetURL in stylesheets:
        getHrefPath(urlRedirect, stylesheetURL , originPath)
    logger.info('*********** Resource Download End ***********')


def getSrcPath(urlRedirect, resUrl, originPath, type):
    resUrl = str(resUrl)
    resUrl = resUrl[resUrl.find("src=\"") + 5:]
    resUrl = resUrl[:resUrl.find("\"")]
    resUrl = resUrl.replace("../", "/")
    logger.info(resUrl)
    resPath = resUrl[:resUrl.rfind("/")]
    # ex) assets/js/bootstrap.min.js
    if ("//" not in resUrl):
        mkdir(originPath + resPath)
        copy_file(urlRedirect + "/" + resUrl,originPath + resUrl)
    else:
        # https://maps.googleapis.com/maps/api/js?key=AIzaSyBs
        if("http" in resUrl):
            mkdir(originPath + resPath)
            copy_file(resUrl, originPath + resUrl)
        # //fonts.googleapis.com/css?family=PT+Serif:regular,italic,bold,bolditalic
        else:
            resUrl = resUrl.replace("//", "")
            resPath = resPath.replace("//", "")
            mkdir(originPath + resPath)
            copy_file("http://"+resUrl,originPath + resUrl)


def getHrefPath(urlRedirect, hrefURL, originPath):
    hrefURL = str(hrefURL)
    hrefURL = hrefURL[hrefURL.find("href=\"") + 6:]
    hrefURL = hrefURL[:hrefURL.find("\"")]
    hrefURL = hrefURL.replace("../", "/")
    logger.info(hrefURL)
    hrefPath = hrefURL[:hrefURL.rfind("/")]
    # ex) assets/js/bootstrap.min.js
    if ("//" not in hrefURL):
        mkdir(originPath + hrefPath)
        copy_file(urlRedirect + "/" + hrefURL , originPath + hrefURL)
    else:
        # ex) https://maps.googleapis.com/maps/api/js?key=AIzaSyBs
        if("http" in hrefURL):
            mkdir(originPath+hrefPath)
            copy_file(hrefURL, originPath + hrefURL)
        # ex) //fonts.googleapis.com/css?family=PT+Serif:regular,italic,bold,bolditalic
        else:
            hrefURL = hrefURL.replace("//", "")
            hrefPath = hrefPath.replace("//", "")
            mkdir(originPath + hrefPath)
            copy_file("http://"+hrefURL,originPath + hrefURL)

def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def copy_file(downurl,filename):
    resource = requests.get(downurl).content
    with open(filename, "wb") as code:
        code.write(resource)

def htmlMaker(html, originPath):
    with open(originPath + "index.html", "wb") as code:
        code.write(html)

