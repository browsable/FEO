import socket, ssl,scraping,logging;
logger = logging.getLogger(__name__)
def alpnChecker(url):
    try:
        HOST = url.split("/")[2]
        logger.info('Host is ' + HOST)
        PORT = 443
        ctx = ssl.create_default_context()
        ctx.set_alpn_protocols(['h2', 'h2c', 'spdy/3', 'http/1.1'])
        conn = ctx.wrap_socket(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=HOST)
        conn.connect((HOST, PORT))
        protocal = conn.selected_alpn_protocol()
        logger.info('Secure Checking Complete')
        if(protocal=='h2' or protocal=='h2c'):
            logger.info('Protocal Support '+protocal)
            scraping.resDownload(url)
            return True
        else:
            return False
    except ConnectionError:
        logger.info('Socket ConnectionError')
        return False