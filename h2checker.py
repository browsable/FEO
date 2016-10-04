import requests
import socket
import ssl
# make request headers to check h2c support
headers = {'Accept': '*/*', 'user-agent': 'h2-check/1.0.1', 'Connection': 'Upgrade, HTTP2-Settings',
           'Upgrade': 'h2c', 'HTTP2-Settings': '<base64url encoding of HTTP/2 SETTINGS payload>'}


# http/2 check with h2c
def checkH2(domain):
    # send GET request with the upgrade headers
    r = requests.get('http://' + domain, headers=headers, allow_redirects=True)

    # check the status code if it is 101 Switching Protocols based on http1.1 first
    if r.status_code == 101:
        print('This domain supports HTTP/2 with h2c - HTTP')

    # the status code must be 200 ok or something else based on http1.1 if the server does not support http/2
    else:
        print('This domain does not support HTTP/2 with h2c - HTTP')


# http/2 check with h2
def checkH2S(domain):
    # create a context for communiation
    ctx = ssl.create_default_context()

    # list up protocol candidates
    ctx.set_alpn_protocols(['h2', 'spdy/3', 'http/1.1'])

    # create a socket connection using the context and the fefault https port
    conn = ctx.wrap_socket(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=domain)
    conn.connect((domain, 443))

    # check the selected protocol by the server
    if conn.selected_alpn_protocol() == 'h2':
        print('This domain support HTTP/2 with h2 - HTTPS')
    else:
        print('This domain does not support HTTP/2 with h2 - HTTPS but ' + str(conn.selected_alpn_protocol()))
