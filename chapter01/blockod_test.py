import requests

# 阻塞io
# html = requests.get("http://www.baidu.com")
# print(html.encoding)
# print(html.status_code)
# html.encoding = html.apparent_encoding
# print(html.text)

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "www.baidu.com"
client.connect((host, 80))  # 阻塞IO， cpu空闲
client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format("/", host).encode("utf8"))

data = b""
while True:
    d = client.recv(1024)
    if d:
        data += d
    else:
        break

data = data.decode("utf-8")
print(data)
