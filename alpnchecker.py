import socket, ssl;

def alpnChecker(url):
    try:
        HOST = url.split("/")[2]
        print('HOST is ' + HOST)
        PORT = 443
        ctx = ssl.create_default_context()
        ctx.set_alpn_protocols(['h2', 'h2c', 'spdy/3', 'http/1.1'])
        conn = ctx.wrap_socket(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=HOST)
        conn.connect((HOST, PORT))
        protocal = conn.selected_alpn_protocol()
        print('Next protocol:', protocal)
        if(protocal=='h2' or protocal=='h2c'):
            return True
        else:
            return False
    except ConnectionError:
        print('Socket ConnectionError')
        return False