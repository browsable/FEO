import requests,os,logging
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)

def resDownload(url): #img, js, css
    logger.info('*********** Resource Download Start ***********')

    r = requests.get("http://"+url,allow_redirects=True)

    # scrap list : add tag if you want
    scrapList = ['img','script','data','link']

    # make directory and copy file to local
    download(r,scrapList)

    logger.info('*********** Resource Download End ***********')

def download(r, scrapList):

    urlRedirect = r.url

    originPath = 'origin/' + urlRedirect;  # 사이트 원본 Path
    # optPath = 'opt/' + url_redirect # 사이트 최적화 Path\

    html = r.content
    soup = BeautifulSoup(html, 'lxml')
    for tag in scrapList:
        # ['img','script','data','link']
        if(tag == 'link'):
            srcList = soup.findAll('link', {"type": "text/css", "href": True})
        else:
            srcList = soup.findAll(tag, {"src": True})

        for src in srcList:
            src = str(src)
            if (tag == 'link'):
                src = src[src.find("href=\"") + 6:]
            else:
                src = src[src.find("src=\"") + 5:]
            src = src[:src.find("\"")]
            src = src.replace("../", "/")
            logger.info(src)

            # file path except file name
            filePath = originPath + src[:src.rfind("/")]
            # file path with file name
            fileName = originPath + src

            # ex) assets/js/bootstrap.min.js
            if ("//" not in src):
                mkdir(filePath)
                mkfile(urlRedirect + "/" + src, fileName)
            else:
                # ex) https://maps.googlea....
                if ("http" in src):
                    mkdir(filePath)
                    mkfile(src, fileName)
                # ex) //fonts.googleapis....
                else:
                    srcPath = src[:src.rfind("/")].replace("//", "")
                    src = src.replace("//", "")
                    mkdir(originPath + srcPath)
                    mkfile("http://" + src, originPath + src)

def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def mkfile(downUrl,fileName):
    resource = requests.get(downUrl).content
    with open(fileName, "wb") as code:
        code.write(resource)

def htmlMaker(html, originPath):
    with open(originPath + "index.html", "wb") as code:
        code.write(html)

